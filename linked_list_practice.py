#exercise 1 - Inserting at the end (append)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#class Node and Class linkedList whith the function __init__ are the base for a linkedList

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def insert_at_beggining(self, new_data):
        new_node = Node(new_data) #create a new node
        new_node.next = self.head # we says that the next connection of the new node is the first head, so we move the first to the right
        self.head = new_node #now the new node use the first place of the nodes

        

    def insert_at_end(self, new_data):
        new_node = Node(new_data) # use the class Node with the new_data to create the new node, at this moment this Node doesn't have a head

        #the ex ask to if the list is empty this new node have to be the head of the linkedlist
        if self.head is None:
            self.head = new_node
            return
        #if there is elements in the list, we have to traverse the list until the last element, and add the new node
        last = self.head #we says that the last is the head (the first of the list)

        while last.next: #while last.next isn't None the loop doesn't stop
            last = last.next #updating last to the current head

        #as we find the last node, we assign the new node as the follow node to the last node
        last.next = new_node 

    def print_list(self):
        current = self.head #we says that the current is the head, i mean we start the print with the first element
        output = '' #an empty string with the printed nodes

        while current:  #same: while current is not None:
            output += str(current.data)
            if current.next: #if we have a next node, print a continue text
                output += " -> "
            current = current.next #we continue with the next node
        print(output)

    def delete_head(self):
        if self.head is None: #if the list is empty we don't have anything to delete so the function ends
            return
        self.head = self.head.next #we change the first head to the next of its, and its delete automatically

    def count_nodes(self):
        counter = 0 #initialize the counter with zero
        current = self.head #define the first head

        while current: #while exists a node the while continues
            counter += 1 
            current = current.next
        return counter
        
list1 = LinkedList()

list1.insert_at_end(5)
list1.insert_at_end(10)
list1.insert_at_end(15)
list1.insert_at_beggining(0)

print("the numbers of nodes is: ", list1.count_nodes())

list1.delete_head()
list1.delete_head()

print("the numbers of nodes is: ", list1.count_nodes())

list1.print_list()
