class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next
        temp_node.next = new_node
    
    def remove(self,data):
        temp1_node = None
        temp2_node = self.head

        while temp2_node and temp2_node.data != data:
            temp1_node = temp2_node
            temp2_node = temp2_node.next
        if temp2_node is None:
            return
        if temp1_node is None:
            self.head = temp2_node.next
        else:
            temp1_node.next = temp2_node.next

    def printsll(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data)
            temp_node = temp_node.next

slist = SLinkedList()
# Adding values
slist.append("A")
slist.append("B")
slist.append("C")

# print values
slist.printsll()
print("==============")
# remove values
slist.remove("A")

# print values
slist.printsll()
print("==============")
# remove values
slist.remove("C")

# print values
slist.printsll()