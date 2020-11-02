# Exercise - Create 3 variables to get user data: name, DOB, age

user_name = str(input("Please provide your name "))
user_dob = str(input("Please provide your date of birth in the format - dd/mm/yy "))
user_age = int(input("Please provide your age "))

print('Name: ', user_name)
print('DOB: ', user_dob)
print('Age: ', user_age)

print('Type of variable: ')
print('Name: ', type(user_name))
print('DOB: ', type(user_dob))
print('Age: ', type(user_age))