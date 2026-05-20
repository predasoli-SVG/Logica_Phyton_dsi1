# EX1
# Use a função type() para verificar
# o tipo da variável "ano" com valor 2024.
ano = 2024 
print ("tipo:", type (ano))
print("\n\n")

# EX2
# Verifique se o número 3.14159
# é do tipo float usando isinstance().
numero = 3.14159
print (isinstance(numero, float))
print("\n\n")
# EX3
# Compare se o tipo de 100
# é igual ao tipo de True.
numero = 100
print("compração:", type(100)) == (type(True))
print("\n\n")
# EX4
# Use isinstance() para verificar
# se True pode ser considerado int.
print("considerado:", (isinstance (True, int)))
print("\n\n")
# EX5
# Verifique se o resultado de 5/2
# é do tipo float usando type() e isinstance().
resultado1 = 5/2
print("resultado:", (isinstance (resultado1, float)))

resultado2 = 5/2
print("resultado:", type (resultado2))

# EX6
# Crie uma função que recebe um valor
# e imprime "É número!" se for int, float ou complex.
def verificar(dado):

    if isinstance(dado, (int, float, complex)):
        print("é numérico")
    
    else:
        print("não é numérico")

verificar(42)
verificar("texto")
# EX7
# Compare type() e isinstance()
# para verificar se um booleano
# é considerado inteiro.

valor = True
if type (valor) == int:
    print("type, booleano é inteiro")
else:
    print("type, não é booleano")


# EX8
# Descubra o tipo do número 3+4j
# usando type().
valor = 3+ 4j
print("tipo:", type (valor))
# EX9
# Verifique se o valor None
# é do tipo NoneType usando isinstance().
valor = None
if isinstance(valor, type (None)):
    print("é tipo nonetype")
else:
    print("não é tipo nonetype")
# EX10
# Verifique se o número 3.0
# é int, float ou complex usando isinstance()
# e depois teste especificamente se é int.
numero = 3.0
if isinstance(numero, (int, float, complex)):
    print("É um número")

else:
    print("Não é um número")

if isinstance(numero, int):
    print("É do tipo int")

else:
    print("Não é do tipo int")
