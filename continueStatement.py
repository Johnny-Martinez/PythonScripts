'''
The continue statement is used to tell Python to skip the rest of the statements in the
current loop block and to continue to the next iteration of the loop.
'''

while True:
    s = input('Enter Something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small.')
        continue
    print('input is of sufficent length.')
