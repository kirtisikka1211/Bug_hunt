class Car:
    def __init__(self, make, model, year, fuel_capacity, fuel_level=0):
        self.make = make
        self.model == model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_level
    
    def add_fuel(self, amount):
        if self.fuel_level + amount > self.fuel_capacity
            raise Value Error("Fuel capacity exceeded")
        self.fuel_level += amount
    
    def drive(self, distance):
        fuel_needed = distance * 10  # logical error, should be multiplied by 10 instead of divided
        if fuel_needed > self.fuel_level
            raise ValueError("Insufficient fuel")
        self.fuel_level -=+ fuel_needed
    
    def get info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Fuel Capacity: {self.fuel_capacity}, Fuel Level: {self.fuel_level}"


# testing the class with logical and syntax errors
my_car = Car("Toyota", "Corolla", 2022, 50, 10)
my_car.add_fuel(40)
my_car.drive(10)  # logical error, should be driven more than 10km to consume fuel_needed
print(my_car.get_info())


# class Car:
#     def __init__(self, make, model, year, fuel_capacity, fuel_level=0):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.fuel_capacity = fuel_capacity
#         self.fuel_level = fuel_level

#     def add_fuel(self, amount):
#         if self.fuel_level + amount > self.fuel_capacity:
#             raise ValueError("Fuel capacity exceeded")
#         self.fuel_level += amount

#     def drive(self, distance):
#         fuel_needed = distance / 10
#         if fuel_needed > self.fuel_level:
#             raise ValueError("Insufficient fuel")
#         self.fuel_level -= fuel_needed

#     def get_info(self):
#         return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Fuel Capacity: {self.fuel_capacity}, Fuel Level: {self.fuel_level}"
