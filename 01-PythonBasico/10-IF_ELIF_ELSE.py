var_1 = 'luiz'
var_2 = 'Otavio'
expressao = (var_1 != var_2)
print(expressao)







nome = input('qual seu nome?')
idade = input('qual sua idade?')

idade = int(idade)

idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar emprestimo')
else:
    print(f'{nome} nao pode pegar emprestimo')