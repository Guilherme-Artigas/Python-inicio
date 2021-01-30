frase = 'Curso em Video Python'
print(frase)  # vai apresentar todo o conteudo da frase/string
print(frase[3])  # vai apresentar o conteudo da posição 3 da string. Nesse caso: s
print(frase[3:13])  # apresenta o conteudo que esta dentro da posição 3 e mostra até a 12

print(frase[:15])  # podemos apontar somente o final, nesse caso como nao estamos apontando inicio, começa da posição 0.
print(frase[5:])  # podemos apontar o inicio, sem dizer quando termina, nesse caso vai ate o final da string.

print(frase[0:22:2])
'''
1º argumento/parametro antes do primeiro 2 pontos, indica o inicio.
2º argumento/parametro depois do primeiro 2 pontos e antes do segundo 2 pontos, indica o final.
3º argumento/parametro depois do segundos 2 pontos, indica o salto de casas.
'''

# Frases muito grandes no python, podemos fazer o uso de conjunto de 3 aspas duplas.
print("""Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o 
Fatiamento \nde String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), 
capitalize(), title(), strip(), junção com join().""")
