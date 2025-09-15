nome =input("Digite seu nome: ")
peso =float(input("Digite seu peso: "))
altura =float(input("Digite sua altura: "))

imc = peso / (altura * altura)
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("Peso normal")
elif imc < 29.9:
    print("Sobrepeso")
elif imc < 34.9:
    print("gordo I")
elif imc < 39.9:
    print("gordo II")
else:
    print("gordo III")

print(f" o nome do paciente é: {nome}/nE o imc é: {imc:.2f} ")