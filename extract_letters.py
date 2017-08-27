# Write a script that extracts letters from 26 text files and puts them into a list

# Solution
import glob

letter_list = []
file_list = glob.glob("letters/?.txt")

for file_elem in file_list:
    with open(file_elem, "r") as f:
        letter_list.append(f.read())

print(letter_list)

