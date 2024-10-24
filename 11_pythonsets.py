#Creating and initializing a set
my_cities = {"Kampala", "Kigali", "Nairobi", "Mombasa", "Arusha"}

#printing all the set elements
print(my_cities)

#printing the length of the set
print(len(my_cities))

#printing the type of structure
print(type(my_cities))

my_cities.add("Cape Town")
print(my_cities)

other_cities = {"Nakuru", "Naivasha", "Mwanza", "Jiji", "Busia"}
print(other_cities)
my_cities.update(other_cities)
print(my_cities)

# Sets doesn't run
super_cities = {"New York", "Washington", {"California", "Oakland", "LA"}}
print(super_cities)
