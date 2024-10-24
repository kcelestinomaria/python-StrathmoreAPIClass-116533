first_name = input("First Name: ")
last_name = input("Last Name: ")
location = input("Location: ")
age = input("Age: ")

print(first_name.capitalize())


print(last_name.upper())

print(location.casefold()) # turns into lower case

note = "The quick brown fox jumped over the lazy dog"

print(note.count("dog"))