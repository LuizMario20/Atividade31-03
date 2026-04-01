print ("="*16)
print (" CRIE SUA CONTA")
print ("="*16)

usuario = input("\nDigite seu usuário: ")
senha = input("\nDigite sua senha: ")

if usuario and senha: str
print ("\nUsuário cadastrado!\n")

print ("="*16)
print (" FAÇA SEU LOGIN")
print ("="*16)

list = []
list1 = []

usuario_correto = usuario
senha_correta = senha

while len(list and list1) < 3:

    usuario1 = input("\nDigite seu usuário: ")

    senha1 = input("\nDigite sua senha: ")

    list1.append(usuario1)
    list.append(senha1)

    if senha1 == senha_correta and usuario1 == usuario_correto:
        print ("\nLogin realizado!")
        break

    elif len(list1 and list) < 3:
        print ("Usuário ou senha incorreto!")

    elif len(list1 and list1) == 3 and (senha1 and usuario1) != (senha_correta and usuario_correto):
        print ("Login não encontrado!")