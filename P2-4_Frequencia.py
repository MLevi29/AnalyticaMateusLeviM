
# Criando uma lista com todos os inputs
todosvalores = []
k = 0

while k != 'f':
    k = input('> ')
    list.append(todosvalores, k)


# Selecionando apenas os inteiros da lista de inputs
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
inteirosfinais = []

for i in todosvalores:
    verificacao = []
    for j in i:
        val = j in numeros
        list.append(verificacao, val)

    if (False in verificacao) == False:
        i = int(i)
        list.append(inteirosfinais, i)


# Contabilizar as repetições
list.sort(inteirosfinais)
inteirosutilizados = []

for i in inteirosfinais:
    quantidade = 0
    if (i in inteirosutilizados) == False:
        quantidade = list.count(inteirosfinais, i)
        if quantidade == 1:
            print(f'O número {i} aparece {quantidade} vez')
        else:
            print(f'O número {i} aparece {quantidade} vezes')
        list.append(inteirosutilizados, i)
