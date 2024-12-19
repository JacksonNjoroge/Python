#input() = This is a function that prompts the user to enter data
#          and returns the entered data as a string.

name = input("What is your name? ") 
age = input("How old are you? ")
age = int(age)
age += 1
car = input("What is your dream car? ")

print(f"Hello {name}")
print(f"You are {age} years old")
print(f"{car} is the best!")

print(f"{name} of age {age} loves a {car}")

