# Create a Python function that takes a text file as input and returns the number of words contained in the text file.
# Please take into consideration that some words can be separated by a comma with no space.
# For example "Hi,it's me." would need to be counted as three words.


# Solution

def count_words(filepath):
    with open(filepath) as f:
        data = f.read()
        data.replace(",", " ")
        return len(data.split(" "))

print(count_words("words1.txt"))


