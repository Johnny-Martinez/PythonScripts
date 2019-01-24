'''
Sometimes you may want to define a function that can take any number of
parameters, i.e variable number of arguments, this can be achieved by
using the stars.
'''


def total(a=5, *numbers, **phonebook):
    print('a', a)


# Iterate through all items in a tuple
for single_item in numbers:
    print('single_item', single_item)


for first_part, second_part in phonebook.items():
    print(first_part, second_part)


total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560)
