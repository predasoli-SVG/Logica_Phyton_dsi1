# AULA COMPLETA: NUMERO EM PHYTON
"""
VAMOS APREDER:
1-TIPOS NUMÉRICOS
2-CONVERSÕES DE TIPOS
3-HIERARQUIA NUMÉRICA
4-OPERAÇÕES MATMÁTICAS
4-COERÇÃO DE TIPOS
5-VERIFICÇÃO DE TIPOS
6-ENTRADA DE DADOS
"""

# PASSO 1 - TIPOS NUMÉRICOS #
# INT -> INTEIROS #
# FLOAT -> NÚMERICOS COM CASAS DECIMAIS #
# COMPLEX -> NÚMEROS COMPLEXOS (usado em matematica/engenharia) #

print(" --TIPOS NÚMERICOS-- ")
vendas = 1000

custo = 300
lucro = vendas - custo
print ("o nosso lucro foi de:", lucro, "e a nossas vendas foi de:", vendas)
numeros_interio =10 
#mostrando o valor!!
print("valor:", numeros_interio)

#TYPE () mostra qual é o tipo da variavelag
print("tipo:", type (numeros_interio))

#exemplo 2 - numero decimal
numero_decimal = 3.13
print("tipo:", type(numero_decimal))

#exemplo 3 - numeros cmplexos
#um número complexo possui duas partes:
#numero normal (numero normal)
  #parte imaginária (mutiplicad por j)
#estruturada geral;
#numero =a +bj

# a = parte real
# parte imaginária      
# j = unidade imaginária

numero_complexo = 2+3j
print("valor:", numero_complexo)
print("tipo:", type(numero_complexo))