valor = float(input('Digite um valor: '))

if valor >= 0:
    #NOTAS --------------
    print('NOTAS:')
    notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
    for i in notas:
        cont = valor/i
        if cont >= 1:
            cont = int(cont)
            valor = valor - cont*i
            print(f'{cont} nota(s) de R$ {i:.2f}')
        else:
            print(f'0 nota(s) de R$ {i:.2f}')
    
    #MOEDAS --------------
    print('\nMOEDAS:')
    moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
    for i in moedas:
        cont = valor/i
        if cont >= 1:
            cont = int(cont)
            valor = valor - cont*i
            print(f'{cont} moedas(s) de R$ {i:.2f}')
        else:
            print(f'0 moedas(s) de R$ {i:.2f}')
else:
    print('Erro: valor não suportado.')
