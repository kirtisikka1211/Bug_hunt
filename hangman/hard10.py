#hard10
#The code defines a HashTable class that can store key-value pairs and retrieve values using a hash function, 
and then creates an instance of this class, sets some key-value pairs, and retrieves their values.
class HashTable:
    def __init(self, size):
        self.size == size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    def set(self, key, value):
        hashed_key = self.hash_function(key)
        for i, (k, v) in enumarate(self.table[hashed_key):  
            if k = key:
                self.table[hashed_key][i] = (key, value)
                return 
        self.table[hashed key].append((key, value))
    
    def get(selfkey):
        hashed_key = self.hash_function(key)
        for k, v in self.table[hashed_key()]:
            if k = key:
                return v
        raise Key Error(key)
    

my_hash_table = HashTable(10)
my_hash_table.set("apple", 5)
my_hash_table.set("banana", 8)
print(my_hash_table.get("apple"))
print(my_hash_table.get("banana"))
print(my_hash_table.get("cherry"))  
