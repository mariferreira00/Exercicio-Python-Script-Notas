# cada 2m² de parede precisa de 2 litros de tinta para ser pintado. entenda área como LxA.
l = float(input('Informe a largura da sua parede em metros: '))
a = float(input('Informe a altura da sua parede em metros: '))
areaTotal = l * a
print('A sua parede tem dimensão de {}x{}, sua área é de {}m².' .format(l, a, areaTotal))
tinta = areaTotal / 2
print('Você vai precisar de {} litros de tinta para pínta-la.' .format(tinta))