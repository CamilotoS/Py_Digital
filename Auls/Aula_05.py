# Aula de Lista e Tuplas

# Criando Listas

lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante']

# Pode-se trabalhar varias tipos em uma lista , mas não é aconselhavel

# Vendo Posições na lista
print(lista)
print(lista[3])

print('------------')

print(lista_animal)
print(lista_animal[1])

print('------------')

# Usando for na lista
for x in lista_animal:
    print(x)

print('------------')

# Busca de Itens na Lista

if 'gato' in lista_animal:
    print('Existe um gato na lista')
else:
    print('nada encontrado')

print('------------')

#Duplicar uma Lista

nova_lista = lista_animal * 3
print(nova_lista)

print('------------')

# Inclusão de Itens na Lista

lista_animal.append('cachorrochoro') # o Append e o comando de Inclusão
print(lista_animal)

print('------------')

# Exclusão de Animais na lista

#lista_animal.pop() # retira o ultimo nome da lista
#print(lista_animal)


#lista_animal.pop(2) # Se eu colocar a posição ele remove o item na posição
#print(lista_animal)

print('------------N E W --------')

# Ordenação de Listas

lista.sort()
lista_animal.sort()

print(lista_animal)
print(lista)

print('------------')

# Ordenar a lista de forma reversa

lista.reverse()
lista_animal.reverse()

print(lista)
print(lista_animal)

print('------------')
print(' ')
#Tupla de Listas
# A Lista e mutavel
# Tupla é imutavel

# Declaração de Tupla

tupla = (1, 10, 12, 14,)

print(tupla)
