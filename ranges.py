# 1. Create a script that generates and prints a list of numbers from 1 to 20. Please do not create the list manually.
# 2. Complete the script so that it produces the expected output. Please use my_range  as input data.
#     Expected Output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
# 3. Complete the script so it generates the expected output using my_range  as input data.
#     Please note that the items of the expected list output are all strings.
#     Expected Output: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

# My Solution

array = range(21)
print(array[1:])
print([10 * x for x in array[1:]])
print([str(x) for x in array[1:]])

# Exercise Solution

my_range = range(1,21)
print(list(my_range))
print([10 * x for x in my_range])
print(list(map(str, my_range)))