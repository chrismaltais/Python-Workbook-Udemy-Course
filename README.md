# The Python Workbook: Solve 100 Exercises
My solutions to the Udemy course "The Python Workbook: Solve 100 Exercises" by Ardit Sulce

![alt text](https://udemy-images.udemy.com/course/240x135/1034284_4cad_3.jpg)

## Lessons Learned

**ranges.py**: Array is useful for memory efficiency when everything you need in the list has a fixed type, but it isn't usually faster than using a list.

**simple_dictionary.py**: A `dict` function is another way to create a dictionary. `dict` is also used to convert other objects to a dictionary.

**key_error.py**: A `KeyError` always means Python could not find a key with the name shown next to `KeyError`

**add_dictionary_key.py**: You cannot fix the order of the dictionary items. Dictionaries are unordered collections of items.

**liquid_volume_calculator.py**: Non-default arguments must come before default arguments. i.e. `def foo(b, a= 2):` 
Rule stems from idea: If vice versa occured and only one value was inputted as an argument, would the value be assigned as the default or non-default? Therefore helps simplify

**count_words.py**: Note - this script must run through the file twice, once to replace commas with spaces, then once to split the string using spaces as delimiters. Therefore, if we have _n_ delimiters, we must manually change the code, and will have to run through the file _n_ times. **Not good! :(**

**sequences.py**: `zip()` function: 

```python
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(zipped)
>>> [(1, 4), (2, 5), (3, 6)]
x2, y2 = zip(*zipped)
print(x == list(x2) and y == list(y2))
>>> True
```

**conditioned_letter_extractor.py**: The `glob` module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order. Good for creating a list of required pathnames.
