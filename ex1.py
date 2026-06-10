peso = 10
frete = 10
print("Digite o peso do pacote..")
peso = float(input())
if peso >= 1:
    for i in range(0, 9 + 1, 1):
        print("Digite o peso do pacote novamente.. ")
        peso = float(input())
        print("Digite o destino(Nacional ou internacional)")
        destino = input()
        if destino == "internacional":
            print("Destino intrenacional..")
            if peso < 2:
                print("categoria: Leve ")
                print("seu frete seria de : " + str(frete * 1.2))
            else:
                if peso < 10:
                    print("categoria padrão")
                    print("seu frete = 24")
                else:
                    print("categoria: pesado")
                    print("seu frete = 36")
                print("categoria: padrão")
        else:
            print("Destino nacional..")
            if peso < 2:
                print("categoria: Leve ")
                print("seu frete seria de : " + str(frete))
            else:
                if peso < 10:
                    print("categoria padrão")
                    print("seu frete = 20")
                else:
                    print("categoria: pesado")
                    print("seu frete = 30")
                print("categoria: padrão")
else:
    print("Digite o peso do seu pacote..")
