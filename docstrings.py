'''
Python has a feature called docstrings. Docstrings are used to help document
the program better and makes it easier to understand.
'''


def print_max(x, y):
    '''prints the max of two numbers


    The two values must be integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is the max')
    else:
        print(y, 'Is the max')


print_max(3, 5)
print(print_max.__doc__)

'''
There are two advantages one, being the function is easier since we dont need
to worry about the numbr of arguments. Two, we can give values to only those 
parameters to which we want.
'''
