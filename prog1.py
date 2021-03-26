# Pergunta ao usuario uma nota de 0  a 10 e emite uma mensagem de erro quando  é digitada uma nota inválida.
nota = float(input("Digite uma nota entre 0 e 10: "))
while (nota <= 0 or nota > 10):
    nota = float(input("Nota inválida. Digite uma nota entre 0 e 10: "))
