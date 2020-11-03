# What is a Dictionary?
# Dictionary (arrays) is another way of managing data but more Dynamically
# Key value pairs to store and manage data

# Syntax: {"name" : "James"}
# Understand which brackets work for what i.e. dictionaries, lists, tuples
# What type of data can we store/manage? =====> ANY

# Create a dictionary
devops_students_data = {
    'key' : 'value',
    'name' : 'Matt',
    'stream' : 'tech',
    'completed_lessons' : 4,
    'completed_lesson_names' : ['operators', 'data types', 'variables']
}

print(devops_students_data)
print(type(devops_students_data))

# To print what is stored under name:
print(devops_students_data['name'])

# To see only the keys within a dict
print(devops_students_data.keys())

# To see only the values within a dict
print(devops_students_data.values())

# To fetch the items within the dict etc etc...
print(devops_students_data.items())

# To fetch a particular value from a list within a dict
# e.g. data types from the last key ------>
print(devops_students_data["completed_lesson_names"][1])

# How to change a value of a specific key
devops_students_data["completed_lessons"] = 3
print(devops_students_data["completed_lessons"])


# TASK
# Create a NEW dictionary to store user details

# All the details that you utilised in the last task name, DOB, Address, Course, Grades
# Create a list of hobbies of at least 3..
# Methods of dictionary to remove, add, replace, display the type of items
# Display data in reverse order of hobbies list

sparta_user_details = {
    'first_name' : 'Charlie',
    'last_name' : 'Shelby',
    'dob' : '22/10/1997',
    'address' : '74 Privet Drive',
    'course' : 'DevOps',
    'grades' : ['A', 'A', 'A'],
    'hobbies' : ['running', 'reading', 'hunting']
}
# Deleting dob from the dict
print(sparta_user_details)
del sparta_user_details["dob"]

print(sparta_user_details)

# Adding in 'height' to the dict
sparta_user_details['height'] = 184
print(sparta_user_details)

# for loop cycles through the values and fetches their types()
for i, j in sparta_user_details.items():
    print(type(j))

# Printing out the hobbies list in reverse
print(sparta_user_details['hobbies'][::-1])
print(sparta_user_details)