def selection_sort(array):
    count = 0
    for i in range(len(array)-1): 
        print(array)
        minimum = array[i] 
        minimum_index = i 
        for j in range(i+1,len(array)):
            count += 1
            if array[j] < minimum: 
                minimum = array[j]
                minimum_index = j
        if minimum_index != i: 
            array[minimum_index], array[i] = array[i], array[minimum_index]
    return (f'{array} \nNumber of comparisons = {count}')

array = [5,9,3,10,45,2,0]
print(selection_sort(array))

sorted_array = [5,6,7,8,9]
print(selection_sort(sorted_array))
