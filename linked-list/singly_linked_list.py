class Node:
    """ Node containing a single piece of data. """
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    """ Singly LinkedList, made up of connected Nodes. """
    def __init__(self, data=None):
        if data:
            self.head = Node(data)
        else:
            self.head = None

    def __repr__(self):
        ll_to_arr = []
        cur = self.head
        while cur != None:
            ll_to_arr.append(str(cur.data))
            cur = cur.next
        return ','.join(ll_to_arr)

    def append(self, data):
        """ Append data to the end of a LinkedList.
            Runtime: O(1) if we have a reference to the end, O(n) otherwise
        """
        if self.head == None:
            self.head = Node(data)
        else:
            cur = self.head
            while(cur.next != None):
                cur = cur.next
            cur.next = Node(data)

    def prepend(self, data):
        """ Prepend data to the beginning of a LinkedList.
            Runtime: O(1)
        """
        if self.head == None:
            self.head = Node(data)
        else:
            cur = Node(data)
            cur.next = self.head
            self.head = cur

    def delete_by_value(self, data):
        """ Delete first Node with a given value.
            Runtime: O(1) if we have a reference to the node to delete.
                    beginning of list: O(1).
                    middle of list: search time (~O(n)) + O(1).
                    end of list: O(n) with no reference to end of list.
        """
        if self.head == None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        if self.head.next == None:
            return
        cur = self.head
        while cur.next != None and cur.next.data != data:
            cur = cur.next
        if cur.next:
            if cur.next.data == data:
                cur.next = cur.next.next
        else:
            return
