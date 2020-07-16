# class HashTable:
#     def __init__(self):
#         self.size = 10
#         self.hashmap = [[] for _ in range(0, self.size)]

#     def hashing_func(self, key):
#         hashed_key = hash(key) % self.size
#         return hashed_key

#     def set(self, key, value):
#         hash_key = self.hashing_func(key)
#         key_exists = False
#         slot = self.hashmap[hash_key]
#         for i, kv in enumerate(slot):
#             k, v = kv
#             if key == k:
#                 key_exists = True
#                 break

#         if key_exists:
#             slot[i] = ((key, value))
#         else:
#             slot.append((key, value))

#     def get(self, key):
#         hash_key = self.hashing_func(key)
#         slot = self.hashmap[hash.key]
#         for kv in slot:
#             k, v = kv
#             if key == k:
#                 return v
#             else:
#                 raise KeyError('does not exist.')

# h = HashTable()
# h.set('2001', 'value 1')
# h.set('2002', 'value 2')
# h.set('2003', 'value 3')
# h.set('2004', 'value 4')
# h.set('2005', 'value 5')
# h.set('2006', 'value 6')
# h.set('2007', 'value 7')
# h.set('2008', 'value 8')
# h.set('2009', 'value 9')
# h.set('2010', 'value 10')
# print(h.hashmap)
# print(h.get("2001"))


    