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

print("tamanho ", len(st))


