class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def insert(self, value):
        newNode = Node(value)
        if (self.head == None):
            self.head = newNode
            self.tail = newNode
            self.length += 1
            return 1
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
            return 1

    def printElements(self):
        if (self.head == None): return None
        else:
            temp = self.head

            while (temp):
                print(temp.value, end="--->")
                temp = temp.next

# doubly linked list

    def insertInMid(head, node):
        #code here
        length = findLength(head)
        if (length == 0): return 0
        middle_index = length / 2

        temp = head
        parent_pointer = None
        i = 1
        while temp is not None:
            if (i == middle_index):
                #add to the right
                suffix_node = temp.next

                temp.next = node
                node.next = suffix_node

            else:
                parent_pointer = temp
                temp = temp.next
                i += 1

    def reverse(self):
        # first iterative

        first = self.head
        second = first.next
        self.tail = self.head

        while (second):
            third = second.next
            second.next = first
            first = second
            second = third

        self.head.next = None
        self.head = first
        return self.printElements()

    def duplicateElement(self):
        if not self.head: return None

        temp = self.head
        while temp.next != None:
            if (temp.value == temp.next.value):
                suffix = temp.next
                temp.next = suffix.next
            else:
                temp = temp.next

        return self.printElements()

#floyed cycle detection algorithim.

    def check_cycle(self):
        fast_ptr = self.head
        slow_ptr = self.head
        while (slow_ptr and fast_ptr and fast_ptr.next):
            if (slow_ptr == fast_ptr): return True
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
