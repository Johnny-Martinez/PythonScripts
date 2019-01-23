number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations! you guessed it. ')
        # this causes the while loop to stop.
        running = False
    elif guess < number:
        print('No, its a little higher than that.')
    else:
        print('No its a little lower than that.')
else:
    print('The while loop is over.')

print('Done!')


'''
Example of while loop
while True:
    s = input('enter something : ')
    if s == 'quit':
        break
    print('Length of string is', len(s))
print('done')
'''
