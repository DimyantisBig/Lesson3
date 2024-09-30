num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2 if num2  !=0 else 'Деление на ноль не возможно!'

print(f'Сумма : {sum_result}')
print(f'Разность : {sub_result}')
print(f'Произведение : {mul_result}')
print(f'Частность : {div_result}')

