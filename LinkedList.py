class LinkedList:

    def __init__(self):
        self.head = None


    def reverse(self, current, previous):
        # Mark head if last node
        if current.next is None:
            self.head = current
        # Update the next node
            current.next = previous
            return

        next = current.next
        current.next = previous
        self.reverse(next, current)

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
