# Sets and Frozen Sets - data collection
# indexing - THERE IS NOINDEXING IN SETS
# Sets are unordered
# Syntax: {} brackets for sets

# Sets are good for storing unique values in a
# list that is "unpredictable" per say, its used in hashing mainly,
# for storing random info, their uses are very limited if at all

car_parts = {'Wheels', 'Doors', 'Radio'}
print(car_parts)

# Managing data with sets
# Adding in parts ----->
car_parts.add('seat belt')
print(car_parts)

# Remove parts ----->
car_parts.remove('Wheels')
print(car_parts)