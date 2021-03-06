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
        O(n^2) always because iterates through the hash table in a nested for loop"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        O(n^2) always iterates through the hash table in a nested for loop"""
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        O(n) always iterates through the hash table in a for loop"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        O(n*k) always iterates through the buckets, and the items in those buckets"""
        counter = 0
        for bucket in self.buckets:
            counter += bucket.size
        return counter

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        O(n) constant time complexity"""
        bucket = self.buckets[self._bucket_index(key)]
        for i in bucket.items():
            if i[0] == key:
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        O(n)"""
        index = self._bucket_index(key)
        for item in self.buckets[index].items():
            if item[0] == key:
                return item[1]
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        O(n)"""
        bucket = self.buckets[self._bucket_index(key)]
        if self.contains(key):
            self.delete(key)
        bucket.prepend((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        O(1) always iterates through the hash table in a nested for loop"""
        bucket = self.buckets[self._bucket_index(key)]
        item = bucket.find(lambda data: data[0] == key)
        if item:
            bucket.delete(item)
        else:
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
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
    delete_implemented = True
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
