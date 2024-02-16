class Person:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


# Creating an instance of the Person class
students = Person(['Ehsan', 'James', 'Lars', 'Kirk', 'Robert'])

# Using a loop to read data from the instance
for name in students:
    print(name)
