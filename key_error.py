# Explain what the error displayed on console means and why we get it

d = {"Name": "John", "Surname": "Smith"}
print(d["Smith"])

# Solution

# There is no key Smith  in the dictionary. Smith  is a value. You want to use Surname if you want to access Smith :
#
# print(d["Surname"]
#
# A KeyError always means Python could not find a key with the name shown next to KeyError (e.g. Smith ).