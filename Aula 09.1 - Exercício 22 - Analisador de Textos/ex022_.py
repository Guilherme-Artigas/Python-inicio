nome = input('Digite seu nome completo: ').strip()  # a função pode ser usada na coleta do dado! show :D

print()

print('Seu nome com todas as letras MAIUSCULAS é:', nome.upper())
print('Seu nome com todas as letras minusculas é:', nome.lower())
print('Quantas letras ao todo (sem considerar espaço): {} letras.'.format(len(nome) - nome.count(' ')))
# print('Quantidade de letras do seu 1º nome: {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))
