class HashTable:

    def __init__(self):
        self.size = 10
        self.hashmap =[[] for _ in range(0, self.size)]
        # print(self.hashmap)


    def hashing_func(self,key):
        hashed_key = hash(key) % self.size
        return hashed_key
        

    def set(self,key,value):
        hash_key = self.hashing_func(key)
        key_exists = False
        slot = self.hashmap[hash_key]
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists = True
                break

        if key_exists:
            slot[i] = ((key, value))
        else:
            slot.append((key, value))

    def get(self,key):
        hash_key = self.hashing_func(key)
        slot = self.hashmap[hash_key]
        for kv in slot:
            k, v = kv
            if key == k:
                return v
            else:
                raise KeyError('does not exist.')


H = HashTable()

H.set('2001', 'value1')
H.set('2002', 'value2')
H.set('2003', 'value3')
H.set('2004', 'value4')
H.set('2005', 'value5')
H.set('2006', 'value6')
H.set('2007', 'value7')
H.set('2008', 'value8')
H.set('2009', 'value9')
H.set('2010', 'value10')
print(H.hashmap)



