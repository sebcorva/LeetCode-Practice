#define a node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #star as none, because it is the next node adn it is not defined yet
#linked list
class linkedList:
    def __init__(self):
        self.head = None #start as none, because is the first node and it is not defined yet

    #insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data) #create a new node
        #.next is an attribute of the node class that points to the next node connected to it
        new_node.next = self.head #point the new node to the previous head to connect the new node to the linked list
        self.head = new_node #update the head to the new node
    
    #print the linked list
    def print_linked_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next #move to the next node
        print("->" .join(elements) + "->None")

mi_linked_list = linkedList() #assing the linked list to a variable
mi_linked_list.insert_at_beginning(10)
mi_linked_list.insert_at_beginning(20)
mi_linked_list.insert_at_beginning(30)

mi_linked_list.print_linked_list()