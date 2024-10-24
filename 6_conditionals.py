print("Please enter your age")

age = int(input("Age: "))

if age >= 21: # if evaluates a given condition
    print("Eligible to drive PSV") # execute if true

elif age >= 18: # evaluate if condition 1 is false
    print("Eligible to drive private car only")

else: # evaluates if second condition is false
    print("Not eligible to drive") # execute if true

