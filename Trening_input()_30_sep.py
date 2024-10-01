name = input('Add your name: ')
print(f'Hello {name}')
print('---' * 25)
num1 = float(input('Enter your first number: '))
num2 = float(input('Enter your second number: '))
result = num1 + num2
print(f'Your result is {result}')
print('---' * 25)
num = int(input('Enter your number: '))
if num % 2 == 0:
    print(f'{num} is an even number')
else:
    print(f'{num} is an odd number')