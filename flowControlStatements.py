number = 23
guess = int(input('Enter a number : '))

if guess == number:
    # new block starts here
    print('Congrats!!! you guessed it.')
    print('(but you dont win any prizes!)')
elif guess < number:
    print('No, it is a little higher than that.')
else:
    print('No, it is a little lower than that')

print('Done!')
