from collections import defaultdict

# class TrieNode:
#     def __init__(self, char):
#         self.children = []
#         self.isWord = False
#         self.val = char

# class Trie(object):

#     def __init__(self):
#         self.root = TrieNode('*')        

#     def insert(self, word):
#         current = self.root
#         for w in word:
#             flag = False
#             for child in current.children:
#                 if child.val == w:
#                     flag = True
#                     current = child
#                     break
#             if not flag:
#                 new_node = TrieNode(w)
#                 current.children.append(new_node)
#                 current = new_node
#         current.isWord = True

#     def search(self, word):
#         current = self.root
#         for w in word:
#             found = False
#             for child in current.children:
#                 if child.val == w:
#                     found = True
#                     current = child
#                     break
#             if not found:
#                 return False
#         return current.isWord
        

#     def startsWith(self, prefix):
#         current = self.root
#         for w in prefix:
#             found = False
#             for child in current.children:
#                 if child.val == w:
#                     found = True
#                     current = child
#                     break
#             if not found:
#                 return False
#         return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(hello)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# class TrieNode:
#     def __init__(self, char):
#         self.children = []
#         self.isWord = False
#         self.val = char

# class Trie(object):

#     def __init__(self):
#         self.root = TrieNode('*')        

#     def insert(self, word):
#         current = self.root
#         for w in word:
#             flag = False
#             for child in current.children:
#                 if child.val == w:
#                     flag = True
#                     current = child
#                     break
#             if not flag:
#                 new_node = TrieNode(w)
#                 current.children.append(new_node)
#                 current = new_node
#         current.isWord = True

#     def search(self, word):
#         current = self.root
#         for w in word:
#             found = False
#             for child in current.children:
#                 if child.val == w:
#                     found = True
#                     current = child
#                     break
#             if not found:
#                 return False
#         return current.isWord
        

#     def startsWith(self, prefix):
#         current = self.root
#         for w in prefix:
#             found = False
#             for child in current.children:
#                 if child.val == w:
#                     found = True
#                     current = child
#                     break
#             if not found:
#                 return False
#         return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert("pello")
# obj.insert("pelloworld")
# param_2 = obj.search("word")
# param_3 = obj.startsWith("p")
# print(param_3)

