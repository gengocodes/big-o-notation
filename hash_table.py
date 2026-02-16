class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # list of buckets

    def _hash(self, key):
        # sum of ordinals modulo table size
        return sum(ord(char) for char in str(key)) % self.size

    def set(self, key, value):
        index = self._hash(key)
        # Check if key exists, update if yes
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Else, append new key-value
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # not found

    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

# Demo execution
if __name__ == '__main__':
    ht = HashTable()
    
    ht.set('apple', 10)
    ht.set('banana', 20)
    ht.set('orange', 30)

    print("Get apple:", ht.get('apple'))  # 10
    print("Get banana:", ht.get('banana'))  # 20
    print("Get orange:", ht.get('orange'))  # 30

    ht.set('apple', 50)
    print("Updated apple:", ht.get('apple'))  # 50

    ht.delete('banana')
    print("Get banana after delete:", ht.get('banana'))  # None
