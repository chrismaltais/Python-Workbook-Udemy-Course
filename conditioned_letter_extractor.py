# Write a script that iterates through each of the 26 text files,
# Checks if the letter inside the text file is in the string "python",
# Puts the letter in a list if it's a character of "python"

import glob, math

letters = []
file_list = glob.iglob("letters/?.txt")
letters_wanted = list("python")

for file_elem in file_list:
    with open(file_elem, "r") as f:
        letter = f.read()
        if letter in letters_wanted:
            letters.append(letter)

print(letters)
