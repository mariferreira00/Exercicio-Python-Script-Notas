habA = 0
habB = 0
taxaA = 0
taxaB = 0

while habA < 1:
  habA = int(input('Informe a população do país A '))

while habB < 1:
  habB = int(input('Informe a população do país B '))

while taxaA <= 0:
  taxaA = float(input('Informe a taxa de crescimento da população do país A '))

while taxaB <= 0:
  taxaB = float(input('Informe a taxa de crescimento da população do país B '))

anos = 0
while habA < habB:
  anos  += 1
  habA += round((habA*taxaA/100))
  habB += round((habB*taxaB/100))

print('Em '+ str(anos) + ' anos a população do país A será maior que a população do país B')
print('Habitantes país A = ' + str(habA) )
print('Habitantes país B = ' + str(habB) )