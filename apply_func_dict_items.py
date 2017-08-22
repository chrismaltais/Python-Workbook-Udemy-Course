# Calculate the sum of all dictionary values.
# Filter the dictionary by removing all items with a value of greater than 1, but keeping strings.

d = {"a": 1, "b": 2, "c": 3, "d": 'hello'}
# print(sum(d.values()))

d_filtered = dict((key, value) for key, value in d.items() if value <= 1 or type(value) is str)

print(d_filtered)