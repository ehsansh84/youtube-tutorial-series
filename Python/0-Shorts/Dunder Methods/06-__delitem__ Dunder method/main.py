class CustomList:
    def __init__(self):
        self.items = {}

    def __delitem__(self, index):
        del self.items[index]


# Creating an instance of the CustomList class
my_list = CustomList()

# Assign values
my_list.items = {
    0: 'apple',
    1: 'banana',
    2: 'orange'
}

# Displaying the items before deletion
print("Items before deletion:", my_list.items)

# Using __delitem__ to delete an item
del my_list[1]

# Displaying the items after deletion
print("Items after deletion:", my_list.items)
