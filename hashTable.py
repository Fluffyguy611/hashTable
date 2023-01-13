class HashTable:
    def __init__(self, size):
        # Initialize the hash table with the given size
        self.size = size
        self.filled = 0
        self.table = [None] * self.size
        self.order = []
        self.DEL = 0

    def hashFunction(self, word):
        hash_value = len(word)
        for ch in word:
            hash_value += ord(ch)

        return hash_value % self.size

    def insert(self, key, value):
        if self.ifFullDelete():
            self.deleteEverySecond()
        hash_value = self.hashFunction(key)
        i = 1
        while self.table[hash_value] is not None:
            if i >= self.size*2:

                raise OverflowError("Hashing is taking too long", i, self.filled)

            # Quadratic probing to find the next available slot
            hash_value = (hash_value + i**2) % self.size
            i += 1
        self.table[hash_value] = (key, value)
        self.order.append(hash_value)
        self.filled += 1


    def search(self, key):
        # Search for the given key in the hash table
        hash_value = self.hashFunction(key)
        i = 1
        while self.table[hash_value] is not None:
            if self.table[hash_value][0] == key:
                return self.table[hash_value][1]
            # Quadratic probing to find the next slot to check
            hash_value = (hash_value + i**2) % self.size
            i += 1
        return None

    def delete(self, key):
        # Delete the given key from the hash table
        hash_value = self.hashFunction(key)
        i = 1
        while True:
            if self.table[hash_value] is not None:
                if self.table[hash_value][0] == key:
                    self.table[hash_value] = None
                    self.order.remove(hash_value)
                    self.filled -= 1
                    return
            # Quadratic probing to find the next slot to check
            hash_value = (hash_value + i**2) % self.size
            i += 1

    def ifFullDelete(self):
        if (self.filled/self.size) >= 0.80:
            return True
        return False

    def deleteEverySecond(self):
        # Delete every second key from the hash table
        lst = self.order.copy()
        DEL  = 0
        for i, slot in enumerate(lst):
            if self.table[slot] is not None and i % 2 == 1:
                delete = self.table[slot][0]
                DEL += 1
                self.delete(delete)

        self.DEL = DEL
