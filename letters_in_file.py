# Create a script that generates a text file with all letters of English alphabet inside it, one letter per line.

# Solution
import string

with open("alphabet.txt", "w") as f:
    for letter in string.ascii_lowercase:
        f.writelines(letter + "\n")



