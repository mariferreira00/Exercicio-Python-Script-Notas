# Banco Blue
# Programa coleta informações como : usuário e senha, validação de senha, e mais dados como idade, endereço e saldo, operações do tipo : depósito, saque (com validação de valor) e consulta de saldo.

def Deposito():
    return saldo + deposit

def Saque () :
    return saldo - saq

dados = []
user = input("Informe seu nome de usuário: ")
dados.append(user)
senha = input("Informe a sua senha")
if len(senha) <6 :
    senha = input("Digite novamente, a senha precisa ter pelo menos 6 dígitos:")
idade = int(input("Informe a sua idade: "))
dados.append(idade)
end = input("Informe seu endereço: ")
dados.append(end)
saldo = 1000
dados.append(saldo)

print('.........................SUAS INFORMAÇÕES.........................')
print(f'\tNOME DO USUÁRIO: {dados[0]}')
print(f'\tIDADE: {dados[1]}')
print(f'\tENDEREÇO: {dados[2]}')
print(f'\tSALDO ATUAL: R${dados[3]}')
print('...................................................................')


continuar = 'S'
while continuar in 'Ss':
    operacao = input("Qual operação deseja realizar? Digite 1 para DEPÓSITO, 2 para SAQUE, 3 para CONSULTA DE SALDO.")
    if operacao == "1" :
        deposit = float(input("Informe o valor a ser depositado: "))
        saldo=Deposito()
        print(f"Depositamos o valor de R${deposit} na sua conta.")
    elif operacao == "2" :
        saq = float(input("Informe o valor a ser sacado: "))
        if saq > saldo :
            print('Operação inválida, valor de saque é superior ao saldo atual.')
        saldo = Saque()
        print (f"Sacamos o valor R${saq} de sua conta.")
    elif operacao == "3" :
        print(f"Seu saldo atual é de R${saldo}.")

        continuar = input("Deseja continuar: [s,n]")
        if continuar == "n":
            print(">->->->-Obrigada por utilizar o Banco Blue!<-<-<-<-")
