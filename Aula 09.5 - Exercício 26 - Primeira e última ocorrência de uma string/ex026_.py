frase = str(input('Digite uma frase: ')).strip().upper()
print('Quantas vezes a letra A aparece dentro da frase. {} vezes'.format(frase.count('A')))
print('A primeira ocorrencia da letra A foi na posição {}'.format(frase.find('A') + 1))
print('A ultima ocorrencia da letra A é na posição {}'.format(frase.rfind('A')))
