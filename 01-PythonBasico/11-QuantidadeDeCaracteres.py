usuario = input('Digite seu usuario:    ')
qtd_carac = len(usuario)

print(usuario, qtd_carac, type(qtd_carac))

if qtd_carac < 6 :
    print('Voce precisa digitar ao menos 6 caracteres')
else:
    print('Voce foi cadastrado')

##################################################

string1 = input('Digite alguma coisa:   ')
string2 = input('Digite outra coisa:   ')

print(string2.__len__())