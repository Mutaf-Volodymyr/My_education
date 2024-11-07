class Car:
    def __init__(self, text, num):
        self.text = text
        self.num = num

    def add_number(self, add):
        self.num += add


first_car = Car('Ferrari', 2)

second_car = Car('Lamborghini', 3)


print(first_car.__dict__)
first_car.add_number(2)
print(first_car.num)

