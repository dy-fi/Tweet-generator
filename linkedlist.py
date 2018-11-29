class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # size of linked list
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """
        Return a boolean indicating whether this linked list is empty.
        O(1)
        """
        return self.head is None

    def length(self):
        """
        Return the length of this linked list by traversing its nodes.
        O(1)
        """
        return self.size

    def append(self, item):
        """
        Insert the given item at the tail of this linked list.
        O(1)
        """
        new_node = Node(item)

        if (self.head == None):
            self.head = new_node
            self.tail = new_node
            self.size = 1
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
            self.size += 1

    def prepend(self, item):
        """
        Insert the given item at the head of this linked list.
        O(1)
        """
        new_node = Node(item)

        if (self.head == None):
            self.head = new_node
            self.tail = new_node
            self.size = 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def find(self, quality):
        """
        Return an item from this linked list satisfying the given quality.
        O(n)
        Best case: O(1) if head has quality
        Worst case: O(size) if tail is the only node with the given quality
        """
        curr = self.head
        while(curr != None):
            if (quality(curr.data)):
                return curr.data
            curr = curr.next
        return None

    def delete(self, item):
        """
        Delete the given item from this linked list, or raise ValueError.
        O(n)
        Best case: O(1) when item == head
        Worst case: O(size) when item == tail
        """
        curr = self.head
        prev = None
        while (curr != None):
            # if it matches the item
            if (curr.data == item):
                # if head
                if (prev == None):
                    self.head = self.head.next
                else:
                    prev.next = curr.next
                    # if tail
                    if (prev.next == None):
                        self.tail = prev

                # if linked list had 1 node
                if (self.tail != None and self.tail.data == item):
                    self.tail = None
                # if successfully found what to delete
                self.size -= 1
                return
            prev = curr
            curr = curr.next

        # if it didn't break out it means the item was not found in the linked list
        raise ValueError('Could not find {} in given linked list'.format(item))

    def replace(self, item, newData):
        """
        Replace the data of a node instead of deleting it
        O(n)
        """
        curr = self.head
        while(curr != None):
            if curr == item:
                item.data = newData
                break
            curr = curr.next
        # if it didn't break out it means the item was not found in the linked list
        raise ValueError('Could not find {} in the given Doubly Linked List'.format(item))


class DoubleNode(Node):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.last = None

class DoubleLinkedList(LinkedList):

    def __init__(self, items=None):
        self.head = None
        self.tail = None
        size = 0

        if items is not None:
            for item in items:
                self.append(item)
                self.size += 1

    def append(self, item):
        """
        Insert the given item at the tail of this doubly linked list.
        O(1)
        """
        new_node = Node(item)

        if (self.head == None):
            self.head = new_node
            self.tail = new_node
            self.size = 1
        else:
            self.tail.next = new_node
            new_node.last = self.tail
            self.tail = self.tail.next
            self.size += 1

    def prepend(self, item):
        """
        Insert the given item at the head of this linked list.
        O(1)
        """
        new_node = Node(item)

        if (self.head == None):
            self.head = new_node
            self.tail = new_node
            self.size = 1
        else:
            new_node.next = self.head
            self.head.last = new_node
            self.head = new_node
            self.size += 1



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
