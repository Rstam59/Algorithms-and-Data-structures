import heapq

# initializing list
li = [5, 7, 9, 1, 3]

#using heapify to convert list into heap
heapq.heapify(li)

#printing created heap
print("The created heap is : ", end="")
print(list(li))
#The created heap is : [1, 3, 9, 7, 5]


#using heappush() to push elements into heap
heapq.heappush(li, 4)

#printing modified heap
print("The modified heap after push is : ", end="")
print(list(li))
#The modified heap after push is : [1, 3, 4, 7, 5, 9]


#using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))
#The popped and smallest element is : 1


#Creating two identical heaps to demonstrate the difference between heappushpop and heapreplace
li1 = [5, 7, 9, 4, 3]
li2 = [5, 7, 9, 4, 3]
heapq.heapify(li1)
heapq.heapify(li2)

# using heappushpop() to push and pop items simultaneously
print("The popped item using heappushpop() is : ", end="")
print(heapq.heappushpop(li1, 2))
#The popped item using heappushpop() is : 2


# using heapreplace() to push and pop items simultaneously
print("The popped item using heapreplace() is : ", end="")
print(heapq.heapreplace(li2, 2))
#The popped item using heapreplace() is : 3
