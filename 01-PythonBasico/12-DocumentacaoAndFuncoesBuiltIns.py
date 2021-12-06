

num1 = input('Digite alguma coisa:   ')
num2 = input('Digite outra coisa:   ')

num1 = int(num1)
num2 = int(num2)

if is_number(num1) and is_number(num2):
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
else:
    print('erro')