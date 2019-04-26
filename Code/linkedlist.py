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
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes."""
        count = 0
        if (not self.is_empty()):
            current_node = self.head
            while current_node is not None:
                current_node = current_node.next
                count += 1
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list."""
        node = Node(item)
        if (self.tail is None):
            self.head = node
            self.tail = node
        elif (self.head.next is None):
            self.tail = node
            self.head.next = node
        else:
            self.tail.next = node
            self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        node = Node(item)
        # TODO: Prepend node before head, if it exists
        if (self.head is None):
            self.head = node
            self.tail = node
        elif (self.head.next is None):
            self.head = node
            self.head.next = self.tail
        else:
            node.next = self.head
            self.head = node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality."""
        current_node = self.head
        while current_node is not None:
            if quality(current_node.data):
                return current_node.data
            current_node = current_node.next


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        currentNode = self.head
        previousNode = None
        if(not self.is_empty()):
            while currentNode is not None:
                if self.head is self.tail:
                    self.head = None
                    self.tail = None
                if currentNode.data == item:
                    if previousNode is None: 
                        self.head = currentNode.next
                        currentNode.next = None
                        return self.head # Deleted the head
                    elif currentNode.next is None:
                        self.tail = previousNode
                    previousNode.next = currentNode.next
                    return self.head
                previousNode = currentNode
                currentNode = currentNode.next
        raise ValueError('Item not found: {}'.format(item))
                # TODO: Update previous node to skip around node with matching data


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C', "D", "E" ]:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['E']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
