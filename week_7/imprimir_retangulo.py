def imprimir_retangulo():
    largura = int(input("Digite a largura:"))
    altura = int(input("Digite a altura:"))

    contador = 0
    while contador < altura:
        print("#" * largura)
        contador = contador + 1

