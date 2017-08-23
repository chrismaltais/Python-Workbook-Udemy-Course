# The Python Workbook: Solve 100 Exercises
My solutions to the Udemy course "The Python Workbook: Solve 100 Exercises" by Ardit Sulce

![alt text](https://udemy-images.udemy.com/course/240x135/1034284_4cad_3.jpg)

## Lessons Learned

**ranges.py**: Array is useful for memory efficiency when everything you need in the list has a fixed type, but it isn't usually faster than using a list.

**simple_dictionary**: A `dict` function is another way to create a dictionary. `dict` is also used to convert other objects to a dictionary.

**key_error**: A `KeyError` always means Python could not find a key with the name shown next to `KeyError`

**add_dictionary_key**: You cannot fix the order of the dictionary items. Dictionaries are unordered collections of items.

**liquid_volume_calculator**: Non-default arguments must come before default arguments. `def foo(b, a= 2):` 
Rule stems from idea: If vice versa occured and only one value was inputted as an argument, would the value be assigned as the default or non-default? Therefore helps simplify
