nome = input("Digite seu mome: ")
altura = float(input("Digite sua  altura: "))
peso = float (input("digite seu peso: "))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("Peso normal")
elif imc < 29.9:
    print("Sobrepeso")
elif imc <34.9:
    print("Obsidade Grau I")
elif imc <39.9:
    print("Obsidade Grau II")
else:
    print("Obsidad Grau III (morbida)")


print(f"o nome do paciente é: {nome}\nE o IMC é: {imc}")
