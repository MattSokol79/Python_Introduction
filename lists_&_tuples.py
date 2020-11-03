# Collection in Python
# Lists
# Lists are MUTABLE - CAN BE CHANGED - key difference between lists and tuples
# We can add, remove and change an item in the list
# Indexing starts with 0
# So below: yoghurt is at index 0, apple is at 1 etc etc.
# Syntax: ['yoghurt', 'apple', 'milk']


# Managing lists:
# First list
shopping_list = ['apple', 'milk', 'bread']
print(shopping_list)
print(type(shopping_list))

# Looking at indexing and slicing
print(shopping_list[1]) # To get milk
print(shopping_list[2]) # To get bread
print(shopping_list[1:]) # To get milk and bread

# Add an item to the end of the list
shopping_list.append('eggs')
print(shopping_list) # Adds eggs to the end of the list

# Remove an item from the list
shopping_list.remove('milk')
print(shopping_list) # Removes milk from the list

# Pop deletes the last item from the list
shopping_list.pop()
print(shopping_list) # Removes the last item i.e. eggs from the list
# Pop can be stored in a variable, so can call a variable the pop and it
# saves that item in that variable

# Replacing an item in the list
shopping_list[1] = 'fruits'
print(shopping_list)

# Can we have mixed data types in the list? YES
shopping_list_mixed = [1, 2, 3, 'apple', 'milk', 'bread']
print(shopping_list_mixed)


# TASK - Create a mixed data type list of 7 items
# Display the type of the data
# Add, delete, replace, pop
# Use indexing to print the list in reverse order
mixed_data = [23, 276, 'Olympiad', 'Australia']
print(mixed_data)

# Type of data within the list
for i in mixed_data:
    print(type(i))

# Add 'Maths'
mixed_data.append('Maths')
print(mixed_data)

# Delete 276
mixed_data.remove(276)
print(mixed_data)

# Replace 'Olympiad' with 'Competition'
mixed_data[1] = 'Competition'
print(mixed_data)

# Pop the last item i.e. 'Maths' and store it in a variable - popped_item
popped_item = mixed_data.pop()
print(mixed_data)
print(popped_item)

# Print list in reverse order
mixed_data.reverse() # Or can do print(mixed_data[::-1])
print(mixed_data)


# Tuples
# Tuples are IMMUTABLE - CAN'T BE CHANGED
# Examples of data that NEVER changes: NI number, DOB, Place of Birth
# Syntax: we use () to declare a Tuple

tuple_list = ('paracetamol', 'eggs', 'supermalt')
print(tuple_list)
print(type(tuple_list))
# Cannot add, remove etc etc as this is a tuple
# Changing a tuple to list, changing data and changing back to tuple is
# possible but is a little complicated, and wont be covered in much detail

# Print items in the tuple separately
for i in tuple_list:
    print(i)
# Can also index tuples as with lists so print(tuple_list[0]) to get the
# first item etc etc.

