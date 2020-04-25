class SllNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)
    
    def get_data(self):
        """Return the self.data attribute."""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with new_data parameter."""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """Replace the existing value of the self.next attribute with new_next parameter."""
        self.next = new_next

node = SllNode('apple')
print(node.get_data())
print(node.set_data(7))
print(node.get_data())

node2 = SllNode('carrot')
print(node.set_next(node2))
print(node.get_next())
