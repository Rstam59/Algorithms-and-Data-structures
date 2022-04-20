class Node():
    def __init__(self, data):
        self.data = data 
        self.next = None 



class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1



    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1


    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()

    def insert(self, position, data):
        if position >= self.length:
            if position>self.length:
                print("This position is not available. Inserting at the end of the list")
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        elif position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(position-1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1


    def delete_by_value(self, data):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head == None or self.head.next==None:
                self.tail = self.head
            self.length -= 1
            return
        while current_node.next!= None and current_node.next.data != data:
            #if current_node.data == data:
            #    previous_node.next = current_node.next
            #    return
            current_node = current_node.next
        if current_node.next!=None:
            current_node.next = current_node.next.next
            if current_node.next == None:
                self.tail = current_node
            self.length -= 1
            return
        else:
            print("Given value not found.")



    def delete_by_position(self, position):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        if position == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            self.length -= 1
            return
        if position>=self.length:
            position = self.length-1
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next
        self.length -= 1
        if current_node.next == None:
            self.tail = current_node
        return


if __name__ == '__main__':

    my_linked_list = LinkedList()
    my_linked_list.print_list()
#Empty

    my_linked_list.append(5)
    my_linked_list.append(2)
    my_linked_list.append(9)
    my_linked_list.print_list()
#5 2 9

    my_linked_list.prepend(4)
    my_linked_list.print_list()
#4 5 2 9

    my_linked_list.insert(2,7)
    my_linked_list.print_list()
#4 5 7 2 9

    my_linked_list.insert(0,0)
    my_linked_list.insert(6,0)
    my_linked_list.insert(9,3)
    my_linked_list.print_list()
#This position is not available. Inserting at the end of the list
#0 4 5 7 2 9 0 3

    my_linked_list.delete_by_value(3)
    my_linked_list.print_list()
#0 4 5 7 2 9 0

    my_linked_list.delete_by_value(0)
    my_linked_list.print_list()
#4 5 7 2 9 0

    my_linked_list.delete_by_position(3)
    my_linked_list.print_list()
#4 5 7 9 0

    my_linked_list.delete_by_position(0)
    my_linked_list.print_list()
#5 7 9 0

    my_linked_list.delete_by_position(8)
    my_linked_list.print_list()
#5 7 9
    print(my_linked_list.length)
#3
