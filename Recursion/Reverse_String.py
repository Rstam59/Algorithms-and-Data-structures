def iterative_reverse(string): #Here we use a second string to store the reversed version. Time and Space complexity = O(n)
    reversed_string = ''
    for i in range(len(string)):
        reversed_string = reversed_string + string[len(string)-i-1]
    return reversed_string

print(iterative_reverse("Rustam"))
#matsuR


#Time complexity = O(n). Space complexity = O(n)
def second_iterative_reverse(string):
    original_length = len(string)
    for i in range(original_length):
        string = string + string[original_length - i - 1]
    string = string[original_length:]
    return string

print(second_iterative_reverse("Rustam"))



def recursive_reverse(string):
    print(string)
    if len(string) == 0:
        return string
    else:
        return recursive_reverse(string[1:]) + string[0]

print(recursive_reverse("Rustam"))
