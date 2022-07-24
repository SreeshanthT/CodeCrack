
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self,head=None) -> None:
        self.head = head
    
    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def get_list(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            l_list = []
            while n is not None:
                l_list.append(n.data)
                n = n.ref
            return l_list
    
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.add_begin(data)
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            




if __name__ == "__main__":

    a = LinkedList()
    # a.add_begin(10)
    # a.add_begin(20)
    # a.add_begin(20)
    # a.add_begin(20)
    a.add_end(30)
    print(a.get_list())