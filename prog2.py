# cadastro de usuário - 
print(">>>>>Efetue seu cadastro abaixo<<<<< \n")             
usuario=str(input("Usuário: "))
senha=str(input("Senha: "))
while usuario==senha:
	print("ERRO: usuário e senha não podem ser iguais, tente novamente abaixo: \n")
	usuario=str(input("Usuário: "))
	senha=str(input("Senha: "))
else:
	print("Cadastrado efetuado com sucesso!")
