# class Hashtable(object):

#     def __init__(self, length=4):
#         #Initiate our array with empty values.
#         self.array = [None] * length

#     def hash(self, key):
#         """Get the index of our array for a specific string key"""
#         length = len(self.array)
#         return hash(key) % length

#     def add(self, key, value):
#         """Add a value to our array by its key"""
#         index = self.hash(key)
#         if self.array[index] is not None:
#             # This index already contain some values.
#             # This means that this add MIGHT be an update
#             # to a key that already exist. Instead of just storing
#             # the value we have to first look if the key exist.
#             for kvp in self.array[index]:
#                 # If key is found, then update
#                 # its current value to the new value.
#                 if kvp[0] == key:
#                     kvp[1] == value
#                     break

#                 else:
#                     # If no breaks was hit in the for loop, it 
#                     # means that no existing key was found, 
#                     # so we can simply just add it to the end.
#                     self.array[index].append([key, value])

#     def get(self, key):
#         """Get a value by key"""
#         index = self.hash(key)
#         if self.array[index] is None:
#             raise KeyError()
#         else:
#             # Loop through all key-value-pairs
#             # and find if our key exist. If it does 
#             # then return its value.
#             for kvp in self.array[index]:
#                 if kvp[0] == key:
#                     return kvp[1]

#             # If no return was done during loop,
#             # it means key didn't exist.
#             return KeyError()

#     def is_full(self):
#         """Determines if the HashTable is too populated."""
#         items = 0
#         # Count how many indexes in our array
#         # that is populated with values.
#         for item in self.array:
#             if item is not None:
#                 items += 1
#         # Return bool value based on if the 
#         # amount of populated items are more 
#         # than half the length of the list.
#         return items > len(self.array)/2
        
#     def double(self):
#         """Double the list length and re-add values"""
#         ht2 = Hashtable(length=len(self.array)*2)
#         for i in range(len(self.array)):
#             if self.array[i] is None:
#                 continue
            
#             # Since our list is now a different length,
#             # we need to re-add all of our values to 
#             # the new list for its hash to return correct
#             # index.
#             for kvp in self.array[i]:
#                 ht2.add(kvp[0], kvp[1])
        
#         # Finally we just replace our current list with 
#         # the new list of values that we created in ht2.
#         self.array = ht2.array

#     def __setitem__(self, key, value):
#         self.add(key,value)

# ht = Hashtable()
# # Using __setitem__
# ht["foo"] = "bar"

# # using __getitem__
# val = ht["foo"]

# # using __contains__
# if "foo" in ht:
#     print("Exist!")
    
# # using __iter__
# for kvp in ht:
#     print(kvp)

# a_dict = {'amy': 23, 'tom': 'age unknown'}
# a_dict['george'] = 44

# print(a_dict['george'])

# def appears_twice(given_list):
#     name_dict = {} # {George: 1, Tom: 1}
#     for name in given_list:
#         if name in name_dict:
#             return name
#         else:
#             name_dict [name] = 1
#     return ''

# print(appears_twice(['George', 'Tom', 'Emily', 'Jenny', 'Tom']))

def pair10(given_list):
    numbers_seen = {}
    for item in given_list:
        if (10 - item) in numbers_seen:
            print(str(10 - item) + ',' + str(item))
            return
        else:
            numbers_seen[item] = 1

    print("There is no pair that adds up to 10")

print(pair10([1, 2, 9, 8]))