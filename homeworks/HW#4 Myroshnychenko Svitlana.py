# 1
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# 2
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity


# 3
bus_1 = Bus(max_speed=145, mileage=879, seating_capacity=54)
print(type(bus_1))

# 4
school_bus = Bus(150, 25478, 54)
print(isinstance(school_bus, Vehicle))


# 5
class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


# 6
class SchoolBus(Bus, School):
    def __init__(self, max_speed, mileage, seating_capacity,
                 get_school_id, number_of_students,
                 bus_school_color):
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        School.__init__(self, get_school_id, number_of_students)
        self.bus_school_color = bus_school_color

bus_2 = SchoolBus(max_speed=180, mileage=178, seating_capacity=68, get_school_id=28, number_of_students=245, bus_school_color='yellow')
print(bus_2.max_speed, bus_2.get_school_id, bus_2.bus_school_color)


# 7
class Bear:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(f'The bear {self.sound}s.')


class Wolf:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(f'The wolf {self.sound}s.')

panda = Bear('growl')
wolfy = Wolf('howl')

all_animals_tpl = (panda, wolfy)
for animal in all_animals_tpl:
    animal.make_sound()


# # 8
#
#
# class City:
#     def __init__(self, name, population):
#         self.name = name
#         self.population = population
#
#     def __call__(self):
#         if self.population > 1500:
#             return self.name
#         else:
#             return "Your city is too small"
#
#
# city_1 = City('New York', 8419)
# city_2 = City('Vinnytsya', 1420)
# print(city_1.__call__())
# print(city_2.__call__())
#
# # class City:
# #     def __init__(self, name, population = None):
# #         self.name = name
# #         if population > 1500:
# #             self.population = population
# #         else:
# #             print("Your city is too small")
