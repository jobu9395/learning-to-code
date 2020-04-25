class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine type of this restaurant is {self.cuisine_type}.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!\n")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served
        

chipotle = Restaurant('Chipotle', 'mexican')
chipotle.describe_restaurant()
chipotle.open_restaurant()
chipotle.set_number_served(35)

wendy = Restaurant('Wendys', 'fast-food')
wendy.describe_restaurant()
wendy.open_restaurant()

dunkin = Restaurant('Dunkin Donuts', 'sugary sweets')
dunkin.describe_restaurant()
dunkin.open_restaurant()


class User:
    def __init__(self, first_name, last_name, age, height_inches):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height_inches = height_inches

    def describe_user(self):
        print(f"The user's name is {self.first_name} {self.last_name}.  He is {self.age} years old and is {self.height_inches} tall in inches.\n")

    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}!")


john = User('John', "Smith", 16, 69)
john.describe_user()
john.greet_user()
        
        