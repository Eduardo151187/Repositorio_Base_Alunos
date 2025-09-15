import time

print("--------------------------------")
print("*******🚚 rast 🚚*****")
print("--------------------------------")

usuario = input("Digite o nome de usuario: ")
senha = input("Digite sua senha: ")

print("Carregando ..........")
time.sleep(3)


if usuario == "admin" and senha == "1234":
    print("login bem-sucedido!")
    print("--------------------------------")
    print(f"bem vindo ao rast {usuario}😁😁")
    print("--------------------------------")
else:
    print("Usuário ou senha incorretos. ❌❌❌")
