# 1.
class Laptop:
    def __init__(self):
        battery_1 = Battery('Battery life is 4 hours')
        battery_2 = Battery('Battery life is 12 hours')
        self.batteries = (battery_1, battery_2)


class Battery:
    def __init__(self, battery_life):
        self.battery_life = battery_life


laptop = Laptop()
print(laptop.batteries[0].battery_life)
print(laptop.batteries[1].battery_life)


# 2.
class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    def __init__(self):
        pass


guitar_string = GuitarString()
guitar = Guitar(guitar_string)

# 3.
class Calc:
    @staticmethod
    def add_nums(num1, num2, num3):
        return num1 + num2 + num3


sum = Calc.add_nums(5, 7, 9)
print(sum)

#4.
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pasta({self.ingredients})'

    @classmethod
    def carbonara(cls):
        return cls(['bacon', 'parmesan', 'eggs'])

    @classmethod
    def bolognaise (cls):
        return cls(['forcemeat', 'tomatoes'])


pasta_1 = Pasta.carbonara()
pasta_2 = Pasta.bolognaise()
print(pasta_1)
print(pasta_2)

#5*.
class Concert:
    max_visitors_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value <= self.max_visitors_num:
            self._visitors_count = value
        else:
            self._visitors_count = self.max_visitors_num


Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)


# 6.
import dataclasses


@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    adress: str
    email: str
    birthday: str
    age: int


person = AddressBookDataClass(key = 123, name = 'Bob',
                              phone_number = '0432-52-42',
                              adress ='Soborna str, 50',
                              email = 'mail@email.com',
                              birthday = '15.01.2000',
                              age = 21)
print(person)

#7.

from collections import namedtuple
AddressBookDataClass = namedtuple('AddressBookDataClass', ['key', 'name', 'phone_number', 'address',
                                                           'email', 'birthday', 'age'])
person = AddressBookDataClass(key = 123, name = 'Bob',
                              phone_number = '0432-52-42',
                              address ='Soborna str, 50',
                              email = 'mail@email.com',
                              birthday = '15.01.2000',
                              age = 21)
print(person)


#8.
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBook(key = {self.key}, name = {self.name}, phone_number = {self.phone_number},' \
               f' address = {self.address}, email = {self.email}, birthday = {self.birthday}, ' \
               f'age = {self.age})'

person = AddressBook(key = '123', name = 'Bob', phone_number = '0432-52-42',
                     address = 'Soborna str, 50', email = 'mail@email.com',
                     birthday = '15.01.2000', age = '21')
print(person)

#9.
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def set_age(self, value):
        self.age = value


person_1 = Person("John", 36, "USA")
print(person_1.age)
person_1.set_age(45)
print(person_1.age)

#10.
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

student = Student(0, 'Nick')
setattr(student, 'email', 'mail@email.com')
print(getattr(student, 'email'))


#11*.
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def fahrenheit(self):
        return self._temperature * 1.8 + 32


boiling_temperature = Celsius(100)
print(boiling_temperature.fahrenheit)
