#Iniciar com letra, pode conter numeros, separar _, letras minusculas


nome = 'Guilherme'
print(nome, type(nome))


nome = 'Guilherme'
idade = 31
altura = 1.80
e_maior = idade > 18
data_1 = True
peso = 110

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)

print(nome, 'tem', idade, ' de idade e seu imc é', (peso / (altura * altura)))