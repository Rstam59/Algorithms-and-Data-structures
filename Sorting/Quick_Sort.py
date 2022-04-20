count = 0

def partition(array, left, right):
    smaller_index = left - 1
    pivot = array[right]
    for i in range(left, right):
        global count
        count += 1
        if array[i] < pivot:
            smaller_index += 1
            array[smaller_index], array[i] = array[i], array[smaller_index]
    array[smaller_index+1], array[right] = array[right], array[smaller_index+1]
    print(array)
    return (smaller_index+1)

def quick_sort(array, left, right):
    if left < right:
        partitioning_index = partition(array, left, right)
        print(partitioning_index)
        quick_sort(array,left,partitioning_index-1)
        quick_sort(array,partitioning_index+1,right)

array = [5,9,3,10,45,2,0]
quick_sort(array, 0, (len(array)-1))
print(array)
print(f'Number of comparisons = {count}')
'''
[0, 9, 3, 10, 45, 2, 5]
0
[0, 3, 2, 5, 45, 9, 10]
3
[0, 2, 3, 5, 45, 9, 10]
1
[0, 2, 3, 5, 9, 10, 45]
5
[0, 2, 3, 5, 9, 10, 45]
#Number of comparisons = 14
'''

sorted_array = [5,6,7,8,9]
quick_sort(sorted_array, 0, len(sorted_array)-1)
print(sorted_array)
print(f'Number of comparisons = {count}')
