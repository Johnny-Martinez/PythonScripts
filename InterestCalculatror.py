print("Interest Calculator:")
amount = float(input('what is your principal amount ?'))
roi = float(input('What is the rate of interest ?'))
years = input(input('What is the duration (number of years) ?'))
total = (amount * pow(1 + (roi/100), years))
interest = total - amount
print('\nInterest = %0.2f' % interest)
