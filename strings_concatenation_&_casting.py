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

# EXERCISE: Get user data
# Display message (Your age is + )
# Address - including post code and first line of address - house number
# DOB

user_name = str(input("Please enter your full name "))
user_age = int(input("Please enter your age "))
user_housenumber = int(input("Please enter your house number "))
user_address = str(input("Please enter your street name"))
user_postcode = str(input("Please enter your postcode "))
user_dob = str(input("Please enter your date of birth in the format dd/mm/yy "))

print("Hello " + user_name, "your age is " + str(user_age), "your full address is "
      + str(user_housenumber), user_address, user_postcode, "and your date of birth is "
      + user_dob)

# Or do f" formatting like the example below
print(f"Hello {user_name} yor age is {str(user_age)}, your full address is {str(user_housenumber)}"
      f"{user_address} {user_postcode} and your date of birth is {user_dob}")

# Declaring strings with double and single quotes
# "" as well as ''
single_quotes = 'single_quotes\'wow\''
print(single_quotes)

double_quotes = "double quotes 'wow' "
print(double_quotes)




# String slicing - Why?
# Indexing in python starts from 0
greetings = "Hello World!"

# We only want to print out Hello, prints out from H - space so Hello
print(greetings[0:5])

# How to find the length of string? len()
print(len(greetings))

# How to get rid of these spaces at the end? Its necessary as it consumes memory
white_spaces = "lot's of spaces at the end                                     "
print(len(white_spaces))
print(white_spaces.strip())

# strip() deletes all the spaces at the end of a string
print(len(white_spaces.strip()))




# count() counts number of times any word is available in the string
example_text = "lots of text with Some text "
print(example_text.count("text")
# The output is 2 as the word "text" is in the string twice

# To replace something
print(example_text.replace("with", ",")) # Replace the "with" and put ","

# Capitalise the first letter of the sentence
print(example_text.capitalize())

# Change everything to upper case
print(example_text.upper())

# Change everything to lower case
print(example_text.lower())