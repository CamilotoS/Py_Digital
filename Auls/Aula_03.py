# Condicionais:
# IF
# ELSE
# ELIF
# Operadores Logicos : AND , OR , NOT , or not


# Declaração de Variais

a = int(input('Digite o 1 valor :'))
b = int(input('Digite o 2 valor :'))
c = int(input('Digite o 3 Valor :'))

# Condicional IF

if a > b:
    print('o Numero maior é {}'.format(a))
else:
    print('o maior número é {}'.format(b))

print('Fim da Execução do IF')

#ELIF
if a > b and a > c:
    print('o Numero maior é {}'.format(a))
elif b > a and b > c:
    print('o maior número é {}'.format(b))
else:
    print('o numero maior é {}'.format(c))

print('Fim da Execução do ELIF')


# Saber se o Numero é par

numero = int(input('Digite um valor :'))
resto = numero % 2

if resto == 0:
    print('numero {} é par'.format(numero))
else:
    print('o Numero {} é impar'.format(numero))

print('Fim da Execução dos numeros par')


# Comparação com Operadores logicos

a = int(input('Digite um valor inteiro:'))
b = int(input('Digite um 2 valor Inteiro:'))

resto_a = a % 2
resto_b = b % 2

if resto_a == 0 and resto_b == 0:
    print('O numero digitado é par!')
else:
    print('Numero Digitado é impar!')

print('fim da Execução de Operadores Logicos')

