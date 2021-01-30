km = float(input('Digite a velocidade: '))

if km > 80:
    multa = (km - 80) * 7
    print('Voce foi multado! velocidade excedente a 80KM --> {}'.format(km))
    print('Valor da multa R${:.2f}'.format(multa))
else:
    print('Voce é um homem de bem! sua velocidade {}'.format(km))
