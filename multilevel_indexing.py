# Create a dictionary of keys a, b, and c where each key has as value a list from 1-10, 11-20, and 21-30 respectively
# Access the third value of key b from the dictionary.
# Please complete the script so that it prints out the expected output.
#   Output: b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#           c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
#           a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Solution

from pprint import pprint

d = dict(a=list(range(1, 11)), b=list(range(11, 21)), c=list(range(21, 31)))

pprint(d)

print(d["b"][2])

for k,v in d.items():
    print(k, "has value", v)


