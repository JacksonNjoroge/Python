age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old for this")
elif age >= 18:
    print("Access granted")
elif age < 0:
    print("You are not born yet")
else:
    print("Access denied")