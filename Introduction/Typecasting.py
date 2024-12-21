#Typecasting - This is the process of converting on variable from aone data type to another
#                str(), int(), float(), bool()

name = ""
age = 20
gpa = 4.2
is_Student = False

print(type(is_Student)) #type() function is used to get the variable type

#Converting gpa to int
gpa = int(gpa)
print(gpa)

#Converting int to String
age = str(age)
print(type(age))
print(age)

age += "1"
print(age)

#Converting String to Boolean
name = bool(name)
print(name)