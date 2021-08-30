numero = input("Digite um número inteiro:")

if len(numero) >= 2:
    print(f"O digito das dezenas é {numero[-2]}")
else:
    print("O dígito das dezenas é 0.")