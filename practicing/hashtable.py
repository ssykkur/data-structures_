

class HashTable:

    def __init__(self):
        self.capacity = 10
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def hash_function(self, key):
        hash_sum = 0

        for letter in key:
            hash_sum += ord(letter)

        return hash_sum % self.capacity

    def insert(self, key, data):
        index = self.hash_function(key)

        while self.keys[index] is not None:
            #updating an existing key
            if self.keys[index] == key:
                self.values[index] = data
                return 
            #linear probing
            index = (index + 1) % self.capacity
        #valid slot found
        self.keys[index] = key
        self.values[index] = data

    def get(self, key):
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index + 1) % self.capacity
        
        return None

if __name__ == '__main__':

    table = HashTable()
    table.insert('adam', 23)
    table.insert('kevin', 45)
    table.insert('daniel', 34)
    table.insert('daniel', 33)
    
    

    print(3%10)