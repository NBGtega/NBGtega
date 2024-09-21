#creating a software that allows mr adida keep a record of the cars he has in his car stand
#also allowing customers to search through the cars he's got and recommends a type of car for them to buy.


class Car:
    """ Creating a class for the cars he's got in the car stand"""
    def __init__(self,car_model,type_of_car,name_of_car,make, year_of_prod,price_of_car):
        self.name = name_of_car
        self.model = car_model
        self.type = type_of_car
        self.year = year_of_prod
        self.make = make
        self.price = price_of_car
    
    """Creating a method that fetches each car attributes"""
    def get_name_of_car(self):
        return self.name
    def get_car_model(self):
        return self.model
    def get_type_of_car(self):
        return self.type
    def get_year_of_prod(self):
        return self.year
    def get_make(self):
        return self.make
    def get_price_of_car(self):
        return self.price
    
"""Creating an inventory where cars are added based on Mr adidas input"""

class CarInventory:
    def __init__(self):
        self.cars = []
    
    def add_cars_to_inventory(self,car_model,type_of_car,name_of_car,make, year_of_prod,price_of_car):
        cars = Car(car_model,type_of_car,name_of_car,make, year_of_prod,price_of_car)
        self.cars.append(cars)

    def get_car_model(self,car_model):
        for car in self.cars:
            if car.get_car_model() == car_model:
                return car
        return None
    



#creating a car inventory instance
carinventory = CarInventory()

#creating a loop to add cars to the inventory
while True:
    print("Add a new car to the inventory: ")
    car_model = input("Enter Car model: ")
    type_of_car = input("Enter Type of Car: ")
    name_of_car = input("Enter Name of Car: ")
    make = input("Enter make of Car: ")
    year_of_prod = input("Enter Year of Car production: ")
    price_of_car = input("Enter price of Car production: ")

    another_car = input("Do you want to add another car to the inventory? (Yes/No)")
    another_car.lower()
    if another_car != "yes":
        break

#search for cars
while True:
    print("Search through car model: ")
    search_car_model = input("Type car model to search through:")
    car = carinventory.get_car_model(car_model)
    if car:
        print(f"Found car: {car.make} {car.year}, Price: ${car.price}")
    else:
        print("car not found.")



