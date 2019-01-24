'''
The return statement is used to return from a function, i.e break out of 
the function. We can optionally return a value from the function as well.ArithmeticError
'''


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal.'
    else:
        return y


print(maximum(2, 3))

'''
Note: that a return statement without a value is equivalent to RETURN NONE
NONE is a special type in python that represents nothingness. Its used
to indicate that a variable has no value. 
'''
