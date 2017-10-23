import pdb

class Node (object):
    def __init__ (self, next_node, data):
        self.data = data
        self.next_node = next_node

class LinkedList (object):
    def __init__ (self, array):
        self.head = None;
        previous = None

        for item in array:
            current = Node(Node, item)

            if previous != None:
                previous.next_node = current
            else:
                self.head = current
                
            previous = current

    def print_list():
        n = self.head
        while n is not None :
            print n.data
            n = n.next_node

    # insert to the head
    def insert(self,data):
        n = Node(self.head, data)
        self.head = n

    def delete(data):
        current = self.head
        previous = current
        while current != None:
            if current.data == data:
                previous.next_node = current.next
                current.next = None
                current=None

        
if __name__ == '__main__':
    array = [1,2,3]
    l = LinkedList(array)
    l.print_list
                   

