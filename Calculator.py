num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
op1 = input('Выберите операцию из следующих (+,-,*,/,%,**,//,): ')

if op1 == '+':
    print('Ответ:', float(num1 + num2))
elif op1 == '-':
    print('Ответ:', float(num1 - num2))
elif op1 == '*':
    print('Ответ:', float(num1 * num2)) 
elif op1 == '/':
    if num2 == 0:
        print('На ноль делить нельзя')
elif op1 == '%':
    if num2 == 0:
        print('На ноль делить нельзя')
elif op1 == '**':
    print('Ответ:', int(num1 ** num2))
elif op1 == '//':
    if num2 == 0:
        print('На ноль делить нельзя')
else:
    print('Данной операции нет в системе')                            
    
     