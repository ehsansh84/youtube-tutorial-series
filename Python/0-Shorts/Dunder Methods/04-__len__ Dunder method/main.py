# __len__

class PersonCars:

    def __init__(self, name, cars: list):
        self.name = name
        self.cars = cars

    def __len__(self):
        return len(self.cars)


person_cars = PersonCars(name='Ehsan', cars=['BMW', 'Mercedes Benz'])
person_cars.cars.append('Opel')

print(len(person_cars))
