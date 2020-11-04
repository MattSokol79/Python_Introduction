# How to create a variable
# If you want to comment out more than one line, highlight it all and CTRL + /

name = "Matt" # String
# Creating a variable called name to store user name

age = 22 # Int
# Creating a variable called age to store age of user

hourly_wage = 10 # Int
# Creating a variable called hourly_wage to store the hourly wage of the user

travel_allowance = 2.1 # Float
# Creating a variable called travel_allowance to store the travel allowance of the user

# Python has string, int, float and boolean values
# How to find out the type of variable?
# => type() gives us the actual type of value
print(travel_allowance)
print(age)
print(hourly_wage)


# How to take user data
# Use input() to get data from users

name1 = str(input("Please enter your name "))
# Getting user data by using input() method
print(name1)

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