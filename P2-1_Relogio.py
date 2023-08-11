#Feito por Mateus Levi
i = 0
while i != 'f':
    #receber as horas --------------------------------
    h = -1
    while h < 0 or h > 24:
        h = int(input('Digite as horas: '))
        if h < 0 or h > 24:
            print('Erro: formato inválido. Tente novamente.')

    #facilitador de conversão das horas --------------
    if h >= 12:
        h = h - 12

    #receber os minutos -------------------------------
    m = -1
    while m < 0 or m > 59:
        m = int(input('Digite os minutos: '))
        if m < 0 or m > 59:
            print('Erro: formato inválido. Tente novamente.')

    #obtendo o menor angulo ---------------------------
    angH = h * 30
    angM = m * 6
    menorang = min(angH, angM)
    maiorang = max(angH, angM)
    resultado = maiorang - menorang

    if resultado > 180:
        auxang = min(angH, angM) + 360
        resultado = auxang - maiorang

    #mostrando o resultado ----------------------------
    print(f'Dado o horario {h}:{m}, o menor ângulo entre eles é {resultado}º.')
    i = input('Para encerrar o programa digite \'f\'. Para tentar novamente aperte \'enter\'.' )