#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) we are looping through all the buckets + nodes
        """

        all_keys = []  # O(1)
        for bucket in self.buckets:  # O(n)
            for key, value in bucket.items():  # O(n)
                all_keys.append(key)  # O(1)
        return all_keys  # O(1)

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) we are looping through all the buckets + nodes
        """
        # TODO: Loop through all buckets
        all_values = []  # O(1)
        for bucket in self.buckets:  # O(b)
            for _, value in bucket.items():  # O(n)
                all_values.append(value)  # O(1)
        return all_values  # O(1)

    def items(self):
        """Return a list of all items(key-value pairs) in this hash table.
        Running time: O(n) we are looping through all the buckets + nodes
        """
        all_items = []  # O(1)
        for bucket in self.buckets:  # O(b)
            all_items.extend(bucket.items())  # O(l)
        return all_items  # O(1)

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
         Running time: O(n) we are looping through all the buckets + LinkedList inside of the buckets
         O(b * l(n/b))
         """
        count = 0  # O(1)
        for buckets in self.buckets:  # O(b)
            count += buckets.length()  # O(l)
        return count  # O(1)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
            Best Case: O(1) if we find key in first node.
            Average case: O(l) because we are traversing the linked list and l is the average length of the linked list 
            """
        index = self._bucket_index(key)  # O(1)
        bucket = self.buckets[index]  # O(1)
        if (bucket.find(lambda value: key == value[0]) is None):  # O(l)
            return False  # O(1)
        else:
            return True  # O(1)

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Best Case: O(1) if the bucket does not contain the key.
        Average case: O(l) were using the find method, which is O(l) where l is average length of linked list
        """
        index = self._bucket_index(key)  # O(1)
        bucket = self.buckets[index]  # O(1)
        if bucket.is_empty():  # O(1)
            raise KeyError('Key not found: {}'.format(key))  # O(1)

        key_value = bucket.find(lambda value: key == value[0])  # O(l)
        if key_value is None:  # O(1)
            raise KeyError('Key not found: {}'.format(key))  # O(1)
        else:
            return key_value[1]  # O(1)

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Best case: O(1) if deleteing first node
        Average case: O(l) were using the find method, which is O(l) where l is average length of linked list
        """
        index = self._bucket_index(key)  # O(1)
        bucket = self.buckets[index]  # O(1)

        try:
            self.delete(key)  # O(l)
        except KeyError:  # O(1)
            pass

        bucket.append((key, value))  # O(1)

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
         Best case: O(1) if the bucket is empty / deleting first node
        Average case: O(l) were using the find method, which is O(l) where l is average length of linked list
        """
        index = self._bucket_index(key)  # O(1)
        bucket = self.buckets[index]  # O(1)
        key_value = bucket.find(lambda value: value[0] == key)  # O(l)
        if key_value is None:  # O(1)
            raise KeyError('Key not found: {}'.format(key))  # O(1)
        else:
            bucket.delete(key_value)  # O(n)


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ("V", 4), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
