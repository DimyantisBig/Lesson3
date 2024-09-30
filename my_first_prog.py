
print('My first programm'.upper())
price = float(input('Add your price: '))
summ = float(input('Add your summ: '))

sum_result = price + summ
sub_result = price - summ
mul_result = price * summ
div_result = price / summ if summ !=0 else 'Division by 0 is impossible'

print(f'Total plus : {sum_result}')
print(f'Total minus : {sub_result}')
print(f'Total multipliy : {mul_result}')
print(f'Total split : {div_result}')

