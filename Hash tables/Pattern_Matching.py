def naive_pattern_matching(string, pattern):
    matched_indices = [] 
    l = len(pattern)
    flag = 0 #This flag will be used to check if the pattern has been matched or not
    for i in range(len(string) - l + 1): 
        k = 0
        for j in range(i,i+l): 
            if pattern[k] != string[j]: 
                flag = 1
                break;
            else: #If character matches, we increment k by 1
                k += 1
        if flag==0: 
            matched_indices.append(i)
        flag = 0 #We reset the flag to be 0 for the next window
    if matched_indices:
        return matched_indices
    else:
        return None

string = "AABAACAADAABAABA"
pattern = "AABA"
print(f'Pattern found at {naive_pattern_matching(string,pattern)}')

def rabin_karp(string, pattern, prime):
    n = len(string)
    m = len(pattern)
    h = 1
    d = 256
    p = 0
    t = 0
    flag = 0
    matched_indices = []

  
    for i in range(m-1):
         h = (h*d)%prime

    
    for i in range(m):
        p = (p*d + ord(pattern[i]))%prime
        t = (t*d + ord(string[i]))%prime

    for i in range(n-m+1):
        if p==t:
            for j in range(m): #Comparing every character in the substring whose hash value matchs that of the pattern
                if pattern[j] != string[i+j]:
                    flag = 1
                    break #If a non-matching character is found, we break out of the loop
            if flag == 0:
                matched_indices.append(i)
            else:
                flag = 0
     
        if i<n-m:
            t = ((t - ord(string[i])*h)*d + ord(string[i+m])) % prime
            if t<0:
                t = t+prime

    return matched_indices


print(f'Pattern found at {rabin_karp(string,pattern,11)}')
#Pattern found at [0, 9, 12]




