class Stack():

#The constructor consists of only an empty array as length comes built-in with arrays(lists)
    def __init__(self):
        self.array = []

#In the peek method we access the last element of the array(top element of the stack) by using the built-in length functionality of arrays
    def peek(self):
        return self.array[len(self.array)-1]

#For push operation, we use the built-in append method of lists, which appends/pushes/inserts an element at the end of the list(top of the stack)
    def push(self, data):
        self.array.append(data)
        return

#For pop operation, we use thebuilt-in pop method of lists, which removes the last element of the list(top element of the stack)
#Time complexity of pop operation for the last element of the list is O(1).
    def pop(self):
        if len(self.array)!= 0:
            self.array.pop()
            return
        else:
            print("Stack Empty")
            return

    def print_stack(self):
        for i in range(len(self.array)-1, -1, -1):
            print(self.array[i])
        return



my_stack = Stack()
my_stack.push("Andrei's")
my_stack.push("Courses")
my_stack.push("Are")
my_stack.push("Awesome")
my_stack.print_stack()
#Awesome
#Are
#Courses
#Andrei's

my_stack.pop()
my_stack.pop()
my_stack.print_stack()
#Courses
#Andrei's

print(my_stack.peek())
#Courses

print(my_stack.__dict__)
