# Create a function that generates a file where all letters of English alphabet are listed by "n" on each line.

# Solution
import string


def letters_on_line(n):
    with open("alphabet.txt", "w") as f:
        alphabet = string.ascii_lowercase
        letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
        f.writelines(letters)

test = letters_on_line(5)
