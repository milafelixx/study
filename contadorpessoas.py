#receberá nomes até que se receba a string fim e então será contado quantos nomes existem.
listaNomes = []

while True:
    nome = input()
    if not nome == "fim":
        listaNomes.append(nome)
    else:
        break 


print (len(listaNomes))
