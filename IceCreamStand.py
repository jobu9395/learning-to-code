# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f"The name of the restaurant is {self.restaurant_name}.")
#         print(f"The cuisine type of this restaurant is {self.cuisine_type}.")
#
#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is open!\n")
#
#     def set_number_served(self, number_served):
#         self.number_served = number_served
#
#     def increment_number_served(self, additional_served):
#         self.number_served += additional_served
#
#
# chipotle = Restaurant('Chipotle', 'mexican')
# chipotle.describe_restaurant()
# chipotle.open_restaurant()
# chipotle.set_number_served(35)
#
# wendy = Restaurant('Wendys', 'fast-food')
# wendy.describe_restaurant()
# wendy.open_restaurant()
#
# dunkin = Restaurant('Dunkin Donuts', 'sugary sweets')
# dunkin.describe_restaurant()
# dunkin.open_restaurant()
#
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type = 'ice cream'):
#         """initialize an ice cream stand"""
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = []
#
#     def display_flavors(self):
#         print("\nWe have the following flavors available:")
#         for flavor in self.flavors:
#             print("- " + flavor.title())
#
# Josh_icecream = IceCreamStand('Josh Ice Cream')
# Josh_icecream.flavors = ['vanilla', 'chocolate', 'strawberry', 'jaunt']
#
# Josh_icecream.describe_restaurant()
# Josh_icecream.display_flavors()


# sub class 'admin' 9-7, sub class of 'User'

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


# john = User('John', "Smith", 16, 69)
# john.describe_user()
# john.greet_user()


class Admin(User):
    def __init__(self, first_name, last_name, age, height_inches):
        super().__init__(first_name, last_name, age, height_inches)
        self.privileges = []

    def show_privileges(self):
        print(f"\nThe admin, {self.first_name} {self.last_name}, has the following priveleges:")
        for privilege in self.privileges:
            print("- " + privilege)

josh_the_admin = Admin('Josh', 'Burdett', 26, 69)
josh_the_admin.privileges = ['Can add user', 'Can delete user', 'Can send the user to Tarkov']

josh_the_admin.show_privileges()
