# Concatenate two dictionaries and sort the concatenated dictionary by value

# Creating 2 dictionaries
d1 = {'a': 10, 'b': 8}
d2 = {'d': 6, 'c': 4}

# Concatenating dictionaries
d3 = {**d1, **d2}

# Sorting two dictionaries
d4 = sorted(d3.items(), key=lambda kv: kv[1])

# Printing unsorted and sorted dictionaries
print(d3)
print(d4)
