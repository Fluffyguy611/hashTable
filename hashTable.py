class HashTable:
    def __init__(self, size):
        # Initialize the hash table with the given size
        self.size = size
        self.filled = 0
        self.table = [None] * self.size
        self.order = []

    def hashFunction(self, word):
        hash_value = len(word)
        for ch in word:
            hash_value *= ord(ch)

        return hash_value % self.size

    def insert(self, key, value):
        DEL = "DEL"

        if self.ifFullDelete():
            self.deleteEverySecond()

        hash_value = self.hashFunction(key)
        i = 1
        while not (self.table[hash_value] is None or self.table[hash_value] == DEL):
            if i >= self.size*100:
                raise OverflowError("Hashing is taking too long", i, self.filled, self.table)

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
        DEL = "DEL"
        # Delete the given key from the hash table
        hash_value = self.hashFunction(key)
        i = 1
        while True:
            if self.table[hash_value] is not None:
                if self.table[hash_value][0] == key:
                    self.table[hash_value] = DEL
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
        DEL = "DEL"
        # Delete every second key from the hash table
        lst = self.order.copy()
        for i, slot in enumerate(lst):
            if not (self.table[slot] is None or self.table[slot] == DEL) and i % 2 == 1:
                delete = self.table[slot][0]
                self.delete(delete)

