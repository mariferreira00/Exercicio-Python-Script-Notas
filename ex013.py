# calculadora de reajuste salarial

salario = float(input('Informe o salário atual: '))
reaj = float(input('Qual a porcentagem de aumento? '))
sReaj = salario * reaj/100
print('Um funcionário que ganhava R${:.2f}, com o reajuste de {}% passará a ganhar R${:.2f}. ' .format(salario, reaj, salario+sReaj))