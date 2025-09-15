nome = input("digite seu nome: ")
temperatura = float(input("digite a temperatura: "))

if temperatura <= 37.5:
    print("Temperatura normal")
elif temperatura >=37.5:
    print("Está com febre")

print(f"o nome do paciente é: {nome}\nE o TEMPERATURA é: {temperatura}")