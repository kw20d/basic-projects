print('Claculator.Demo')
a = float (input('Enter first number : '))
b = str(input('choose what to do : '))
c = float (input('Enter second number : '))

if b == '+':
    print(a + c)

if b == '-':
    print(a - c)


if b == '/':
    print(a / c)

else :
    print('Wrong input')