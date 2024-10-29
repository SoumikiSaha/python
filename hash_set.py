# Creating a set
my_set = {1, 2, 3}
print("Original set:", my_set)

# Adding elements
my_set.add(4)
print("After adding 4:", my_set)

# Removing elements
my_set.remove(2)
print("After removing 2:", my_set)

# Checking membership
print("Is 3 in the set?", 3 in my_set)

# Set operations
another_set = {3, 4, 5}
print("Union:", my_set | another_set)
print("Intersection:", my_set & another_set)
print("Difference:", my_set - another_set)
print("Symmetric Difference:", my_set ^ another_set)

# Length of the set
print("Length of the set:", len(my_set))

# Clearing the set
my_set.clear()
print("After clearing:", my_set)
