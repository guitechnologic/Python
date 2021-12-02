#Iniciar com letra, pode conter numeros, separar _, letras minusculas


nome = 'Guilherme'
print(nome, type(nome))


nome = 'Guilherme'
idade = 31
altura = 1.80
e_maior = idade > 18
data_1 = True
peso = 110
imc = peso / (altura * altura)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)

print(f'{nome}, tem, {idade},  de idade e seu imc é, {(peso / (altura * altura)):.2f}')
print(f'{nome}, tem, {idade},  de idade e seu imc é, {(peso / (altura ** 2)):.2f}')

print(f'{nome}, tem, {idade},  anos de idade e seu imc é, {imc:.2f}')

print('{nome}, tem, {idade},  anos de idade e seu imc é, {}'.format(nome, idade, imc))

