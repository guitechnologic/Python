

num1 = input('Digite alguma coisa:   ')
num2 = input('Digite outra coisa:   ')

num1 = int(num1)
num2 = int(num2)

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('erro')