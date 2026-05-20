# EX1
# O usuário digitou "25" como sua idade em um formulário.
# Converta para inteiro e calcule a idade que ele terá
# daqui a 5 anos.
idade = int (input("digite a sua idade.."))
resultado= (idade + 5)
print("tipo:", type (resultado))
print (resultado)

# EX2
# Converta o número de ponto flutuante 7.999
# para inteiro e observe o resultado.
valor =int (7.999)
print ("tipo:", type (valor))

# EX3
# Converta a string "-3.14" para float
# e multiplique o resultado por 2.
valor = float("-3.14")
print("tipo:", type (valor))
print(valor *  2)

# EX4
# Tente converter a string "cento e vinte"
# para inteiro e observe o que acontece.
valor = int  ("cento e vinte")
valor ("classe:", type (valor))
#VALUE ERROR!!

# EX5
# Converta o número 42 para string
# e concatene com a palavra " respostas".
numero = 42
numero_str = str(numero)
print("Ex5:", numero_str + " respostas")


# EX6
# Use a função complex() para criar
# um número complexo com parte real 3
# e parte imaginária 5.
numero_complexo = 3 + 5j
print ("valor:", numero_complexo)
print("tipo:", type(numero_complexo))
# EX7
# Converta o número 0 para booleano
# e mostre o resultado.
valor = 0 
booleano = bool(valor)
print ("resultado:", booleano)

# EX8
# Converta o número -100 para booleano
# e mostre o resultado.
valor = -100
booleano = bool (valor)
print ("resultado:", booleano)

# EX9
# Converta o número 3.1415 para inteiro
# e depois para string, tudo em uma única linha.
print(str(int(3.1415)))

# EX10
# Some um número inteiro (5) com um float (2.3)
# e verifique qual é o tipo do resultado.
valor = int (5)
valor1 = float (2.3)
print ("resultado:", valor + valor1)
