#if = Do some code only IF some condition is true
#     ELSE do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old for this")
elif age >= 18:
    print("Access granted")
elif age < 0:
    print("You are not born yet")
else:
    print("Access denied")


for_sale = False
if for_sale:
    print("This item is for sale.")
else:
    print("This item is NOT for sale.")