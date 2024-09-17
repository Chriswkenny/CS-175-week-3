#CS 175
#Christopher Kenny
#Restaurant

vegetarian = False
vegan = False
gluten_free = False

#Questions for user
list_1 = input("Is anyone in your party vegetarian? ")
if list_1.lower() == "yes":
  vegetarian = True

list_2 = input("Is anyone in your party vegan? ")
if list_2.lower() == "yes":
  vegan = True

list_3 = input("Is anyone in your party gluten-free? ")
if list_3.lower() == "yes":
  gluten_free = True

#List of restaurants
restaurant_1 = "Joe's Gourmet Burgers"
restaurant_2 = "Main Street Pizza Company"
restaurant_3 = "Corner Cafe"
restaurant_4 = "Mama's Fine Italian"
restaurant_5 = "The Chef's Kitchen"

#If/else statements
print("Here are your restaurant choices:")
if not vegetarian and not vegan and not gluten_free:
  print(restaurant_1)
if not vegan and not gluten_free:
  print(restaurant_4)
if not vegan:
  print(restaurant_2)
print(restaurant_3)
print(restaurant_5)

