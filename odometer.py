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

restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()
# instance of the class, 'Restaurant' with two parameters, restaurant_name and cuisine_type assigned in this instance
# call the method describe_restraurant under the instance 'restaurant', which prints name and cuisine type with print statements referencing the class variables

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 430
print("Number served: " + str(restaurant.number_served))
# prints a new line, with the string: "Number served: with the int variable, number served converted to a string, under the instance 'restaurant'

restaurant.set_number_served(1257)
print("Number served: " + str(restaurant.number_served))


while restaurant.number_served < 2000:
    restaurant.increment_number_served(100)
print("Number served: " + str(restaurant.number_served))

