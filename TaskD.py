class HashTable:

    def __init__(self, s):
        self.Size = s
        self.list = [None] * s
    
    def _hashing(self,key):
        if isinstance(key,str):
            hashval = 0
            for char in key:
                hashval = (hashval * 31 + ord(char)) % self.Size
            return hashval
        elif isinstance(key,int):
            return key % self.Size
        else:
            raise TypeError("Unsupported key type")
        
    def insert(self,key,val):
        index = self._hashing(key)

        clon_index = index
        while self.list[index] is not None:
            index = (index + 1) % self.size
            if index == clon_index:
                raise Exception("HashTable is full")
        self.list[index] = val
            


    def get_value(self,key):
        index = self._hashing(key)
        if self.list[index] is not None:
            return self.list[index]
        else:
            raise KeyError("Key is Not Found")
    
    def remove(self,key):
        index = self._hashing(key)
        if self.list[index] is not None:
             self.list[index] = None
        else:
            raise KeyError("Key is Not Found")
        
    def __repr__(self):
        return str(self.list)
    
hash_table = HashTable(5) 

hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")
hash_table.insert("key3", "value3")
hash_table.insert("key4", "value2")
print(hash_table.get_value("key4"))
hash_table.remove("key4")
print(hash_table.get_value("key4"))
