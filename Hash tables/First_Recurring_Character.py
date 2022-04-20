def simple_frc(array):
    dictionary = dict()
    for item in array:
        if item in dictionary:
            return item
        else:
            dictionary[item] = True
    return None

array = [2,1,4,1,5,2,6]


def naive_frc(array):
    l = len(array)
    i= 0
    frc = None
    while(i<l):
        j = i+1
        while(j<l):
            if array[i] == array[j]:
                l = j
                frc = array[j]
                continue
            else:
                j+=1
        i += 1
    return frc

print(naive_frc(array))
