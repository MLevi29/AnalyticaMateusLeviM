#Lista com todas as posições do tabuleiro ---------------------
todaspos = []
for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
    for j in ['1', '2', '3', '4', '5', '6', '7', '8']:
        n = i + j
        list.append(todaspos, n)

pos = 0
#Inicio da verificação
while pos != 'f':

    #Entrada de dados
    pos = input('> ')
    
    #Verificação da validade dos dados
    listvalida = []
    for n in todaspos:
        for k in todaspos:
            l = n + ' ' + k
            list.append(listvalida, l)
    
    if pos in listvalida:

        if pos != 'f':
            lispos = str.split(pos)
            posi = lispos[0]
            posf = lispos[1]

            l0 = posi[0]
            n0 = posi[1]

            #Possibilidades --------------------
            lisL = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            lisN = ['1', '2', '3', '4', '5', '6', '7', '8']

            iL = list.index(lisL, l0)
            iN = list.index(lisN, n0)

            lispossibilidades = []

            #possibilidade: primeira coluna a esquerda
            i = iL - 1
            if (i >= 0) and (i < 8):
                j = iN - 2
                if (j >= 0) and (j < 8): 
                    posEB1 = lisL[i] + lisN[j]
                    list.append(lispossibilidades, posEB1)
                j = iN + 2
                if (j >= 0) and (j < 8):
                    posEA1 = lisL[i] + lisN[j]
                    list.append(lispossibilidades, posEA1)

            #possibilidade: segunda coluna a esquerda
            i = iL - 2
            if (i >= 0) and (i < 8):
                j = iN - 1
                if (j >= 0) and (j < 8): 
                    posEB2 = lisL[i] + lisN[j]
                    list.append(lispossibilidades, posEB2)
                j = iN + 1
                if (j >= 0) and (j < 8):
                    posEA2 = lisL[i] + lisN[j]
                    list.append(lispossibilidades, posEA2)

            #possibilidade: primeira coluna a direita
            i = iL + 1
            if (i >= 0) and (i < 8):
                j = iN - 2
                if (j >= 0) and (j < 8): 
                    posDB1 = lisL[i] + lisN[j]
                    list.append(lispossibilidades, posDB1)
                j = iN + 2
                if (j >= 0) and (j < 8):
                    posDA1 = lisL[i] + lisN[j]
                    list.append(lispossibilidades, posDA1)

            #possibilidade: segunda coluna a direita
            i = iL + 2
            if (i >= 0) and (i < 8):
                j = iN - 1
                if (j >= 0) and (j < 8): 
                    posDB2 = lisL[i] + lisN[j]
                    list.append(lispossibilidades, posDB2)
                j = iN + 1
                if (j >= 0) and (j < 8):
                    posDA2 = lisL[i] + lisN[j]
                    list.append(lispossibilidades, posDA2)

            print(lispossibilidades)
            #Validade da jogada -------------------------
            if (posf in lispossibilidades) == True:
                print('VÁLIDO')
            else:
                print('INVÁLIDO')
    else:
        print('Entrada inválid. Tente novamente.')

print('Fim...')