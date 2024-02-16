class CustomList:
    def __init__(self):
        self.items = {}

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

# Creating an instance of the CustomList class
my_list = CustomList()

# Using __setitem__ to set values
my_list[0] = 'apple'
my_list[1] = 'banana'
my_list[2] = 'orange'

# Using __getitem__ to retrieve values
value_at_index_1 = my_list[1]
value_at_index_2 = my_list[2]

# Displaying the results
print("Items:", my_list.items)
print("Value at index 1:", value_at_index_1)
print("Value at index 2:", value_at_index_2)
