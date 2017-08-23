# Create a function that takes any string as input and returns the number of words for that string.

# Solution

def string_split(string):
    if type(string) is str:
        return len(string.split(" "))
    else: print("Please insert a string!")

print(string_split("Hello, how are you doing today? I'm 48"))
print(string_split(62772))