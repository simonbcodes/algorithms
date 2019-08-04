class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self, data=None):
        if data:
            self.head = Node(data)
        else:
            self.head = None

    def __repr__(self):
        ll_to_arr = []
        cur = self.head
        while(cur != None):
            ll_to_arr.append(str(cur.data))
            cur = cur.next
        return ','.join(ll_to_arr)


    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            cur = self.head
            while(cur.next != None):
                cur = cur.next
            cur.next = Node(data)

    def prepend(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            cur = Node(data)
            cur.next = self.head
            self.head = cur

if __name__ == '__main__':
    ll = LinkedList(3)
    print(ll)
    ll.append(4)
    print(ll)
    ll.prepend(5)
    print(ll)
