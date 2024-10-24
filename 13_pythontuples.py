car_tuple = ("Toyota", "BMW", 25, "Merc")

print(car_tuple)

print(car_tuple[0])

print(len(car_tuple))

#car_tuple[1] = "Mazda"

print(car_tuple)

car_list = list(car_tuple)

# check the type of structure
print(type(car_list))

# modify the list
car_list[1] = "Mazda"

new_car_tuple = tuple(car_list)

#check the new tuple composition
print(new_car_tuple)
print(car_tuple)