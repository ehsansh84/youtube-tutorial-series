class Person:

    def __init__(self, name, family):
        self.name = name
        self.family = family

    def __call__(self, *args, **kwargs):
        print(f"Full name is: {self.name} {self.family}")


# Creating an instance of CallableObject
callable_obj = Person(name='Ehsan',family='Shirzadi')

# Calling the object like a function
callable_obj()
