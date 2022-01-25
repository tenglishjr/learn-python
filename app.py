# Conditional Structures

x = int(input('Enter a number between 1 and 15: '))

if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')

print('All done')

# Try / Except Structure

try:
    y = 'Not a number'
    yy = int(y)
except:
    print('That\'s not a number...')
