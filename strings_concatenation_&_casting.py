# What is concatenation?

first_name = "Matthew"
last_name = "Falcon"
number = "777"
age = 18
# We want to make this look presentable and in 1 line

# print(first_name +" "+ last_name +" "+ age)
# Age cannot be added onto the names as you cant add a str to an int

# ALTERNATIVE METHOD: Comma inputs a space between 2 variables

print(first_name, last_name)

# Casting is used to cast int to str, or the other way around
# Now the below code works as everything is a string (turned age to a string)
print(first_name +" "+ last_name +" "+ str(age))

print(int(number))
print(int(number) + age)




# Different Example
name = input("Please enter your name ")
print("Hello " + name)

# Get user data
# Display message (Your age is + )
# Address - including post code and first line of address - house number
# DOB

user_name = str(input("Please enter your full name "))
user_age = int(input("Please enter your age "))
user_address = str(input("Please enter your first line of address "))
user_postcode = str(input("Please enter your postcode "))
user_housenumber = int(input("Please enter your house number "))
user_dob = str(input("Please enter your date of birth in the format dd/mm/yy "))

print("Hello " + user_name, "your age is " + str(user_age), "your full address is "
      + str(user_housenumber), user_address, user_postcode, "and your date of birth is "
      + user_dob)