# __str__

class Person:

    def __init__(self, name, family):
        self.name = name
        self.family = family

    def __str__(self):
        return f'My name is {self.name}  {self.family}'


person = Person(name='Ehsan', family='Shirzadi')

print(str(person))
print(person.__str__())
