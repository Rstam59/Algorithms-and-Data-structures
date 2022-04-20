import sys
class MaxHeap:


    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

#Method to return the position of parent for the node currently at pos. Because of the 1-indexing the formula for the parents and children becomes simpler
    def parent(self, pos):
        return pos // 2

#Method to return the position of the left child for the node currently at pos
    def left_child(self, pos):
        return 2 * pos

#Method to return the position of the right child for the node currently at pos
    def right_child(self, pos):
        return (2 * pos) + 1


    def is_leaf(self, pos):
        if pos >= (self.size // 2) and pos <= self.size:
            return True
        return False

#Method to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]


    def max_heapify(self, pos):

        #If the node is a non-leaf node and smaller than any of its child
        if not self.is_leaf(pos):
            if (self.Heap[pos] < self.Heap[self.left_child(pos)] or
                    self.Heap[pos] < self.Heap[self.right_child(pos)]):

                #Swap with the left child and heapify the left child
                if self.Heap[self.left_child(pos)] > self.Heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.max_heapify(self.left_child(pos))

                #Swap with the right child and heapify the right child
                else:
                    self.swap(pos, self.right_child(pos))
                    self.max_heapify(self.right_child(pos))

    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element
        current = self.size
        while self.Heap[current] > self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

#Method to print the contents of the heap in a detailed format
    def print_heap(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + " LEFT CHILD : " +
                  str(self.Heap[2 * i]) + " RIGHT CHILD : " +
                  str(self.Heap[2 * i + 1]))

    def extract_max(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.max_heapify(self.FRONT)
        return popped


if __name__ == "__main__":
    my_heap = MaxHeap(15)
    my_heap.insert(5)
    my_heap.insert(3)
    my_heap.insert(17)
    my_heap.insert(10)
    my_heap.insert(84)
    my_heap.insert(19)
    my_heap.insert(6)
    my_heap.insert(22)
    my_heap.insert(9)
    my_heap.print_heap()
    '''
     PARENT : 84 LEFT CHILD : 22 RIGHT CHILD : 19
     PARENT : 22 LEFT CHILD : 17 RIGHT CHILD : 10
     PARENT : 19 LEFT CHILD : 5 RIGHT CHILD : 6
     PARENT : 17 LEFT CHILD : 3 RIGHT CHILD : 9
    '''

    print("The Max val is " + str(my_heap.extract_max()))
    #The Max val is 84

    my_heap.print_heap()
    '''
    PARENT : 22 LEFT CHILD : 17 RIGHT CHILD : 19
    PARENT : 17 LEFT CHILD : 9 RIGHT CHILD : 10
    PARENT : 19 LEFT CHILD : 5 RIGHT CHILD : 6
    PARENT : 9 LEFT CHILD : 3 RIGHT CHILD : 9
    '''

    my_heap.insert(100)
    my_heap.print_heap()
    '''
    PARENT : 100 LEFT CHILD : 22 RIGHT CHILD : 19
    PARENT : 22 LEFT CHILD : 17 RIGHT CHILD : 10
    PARENT : 19 LEFT CHILD : 5 RIGHT CHILD : 6
    PARENT : 17 LEFT CHILD : 3 RIGHT CHILD : 9
    '''

    print(my_heap.Heap[0])
    #9223372036854775807






