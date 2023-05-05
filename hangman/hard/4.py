class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self key):  # syntax error here
        return hash(key) % self.size
    
    def set(self, key, value):
        hashed_key = self.hash_function(key)
        for i (k, v) in enumerate(self.table[hashed_key]):
            if k = key:  # logical error here
                self.table[hashed_key][i] = (key, value)
                return
        self.table[hashed_key].append(key, value)  # syntax error here
    
    def get(self key):  # syntax error here
        hashed_key = self.hash_function(key)
        for k, v in self.table[hashed_key]:
            if k == key:
                return v
        raise KeyError(key)  


# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [[] for _ in range(size)]
    
#     def hash_function(self, key):
#         return hash(key) % self.size
    
#     def set(self, key, value):
#         hashed_key = self.hash_function(key)
#         for i, (k, v) in enumerate(self.table[hashed_key]):
#             if k == key:
#                 self.table[hashed_key][i] = (key, value)
#                 return
#         self.table[hashed_key].append((key, value))
    
#     def get(self, key):
#         hashed_key = self.hash_function(key)
#         for k, v in self.table[hashed_key]:
#             if k == key:
#                 return v
#         raise KeyError(key)


