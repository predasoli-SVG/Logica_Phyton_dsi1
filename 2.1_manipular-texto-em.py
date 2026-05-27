# - crição de string 
# -strings multilinha
# -indices e slices 
# -opreções com strings
# - imutabilidade
# -método úteis
# -formatação de texto
# - Unicode e bytes

#-------------------------#
# 1) CRIAÇÃO DE STRINGES
#-------------------------#
#strings são textos em python
#podem ser criadas usando aspas simpels ou duplas

texto1 = "python"
texto2 = 'curso de python'
texto3 = "copa" 'wrold cup'

print (texto1, texto2, texto3)

#Pyhton permite misturar apps simples e dupplas, dentro das strings sem precisar escpaar caracteristicas

#------------------------
# 2) STRINGS MULTILINHA
#------------------------
#Usando três aspas (""" ou ''') paar criar textos que ocupam várias linhas.

menu = """\ 
uso: programa [opções]
-h Exibe ajudam
-U Url do dataset
"""
print(menu)

#esse formato é muito usado para:
# - Menus
# - documentção
# - textos longos

#---------------------------
# 3) CONCATENÇÃO AUTOMÁTICA
#----------------------------
#Quando duas strings aparcem lado a lado, o python junta automaticamente

textos = ("copa " "2026 " "neymar é show mesmo?" "talvez")
print(textos)

#---------------------------
# 4) STRINGES COMO SEQUÊNCIA
#----------------------------

st = "maracana"
print("primiera letra: ", st[0])
# só exibir a letra m

print("ultima letar: ", st [-1])

print("trecho1:4 ", st [1:4])

print("do inicio até 3 ", st [:3])

print("do 2 até o final:", st [2:1])

#---------------------------
# 5) OPERAÇÕES COM STRINGES 
#----------------------------
#Python permite várias operações com strings 
print("m" in st)
#signficado que a letra "m" existe dentro da string

print("x" not in st)
#significado que "x" não existe na string

print("m" * 20)
#mutiplicado repete a string

print("m" + "maracana")
#operador + concatena strings

#---------------------------
# 6) STRINGES SÃO IMUTÁVEIS 
#----------------------------

 #strings não podem ser alterados diretamente!!
 #isso signfica que o conteudo original não muda.
 #o que acontece é a criação de uma nova string.

texto = "python 3"
#método replace cria uma string
texto = texto.replace("3", "2")

print(texto)

#---------------------------
# 7) MÉTODOS IMPORTANTES 
#----------------------------
#   Strings possuem vários métodos úteis

cidade = "maracana"
#coloca a primiera linha maiuscula
print(cidade.capitalize())

#conta quantas vezes aquela letra
print(cidade.count("a"))

#verificar se começa com  "m"
print(cidade.startswith("m"))

#verificar se termina com "z"
print(cidade.endswith("z"))

frase = "copa de 2002"
print(frase.split(" "))

#---------------------------
# 8) FORMATAÇÃO DE STRING
#----------------------------


print("tamanho ", len(st))


