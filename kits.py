 #empresa dará kits para os funcionários. são 3 kits: V (mulher +30), A (mulher -30) e P (homens). precisa dos dados de nome do funcionário, gênero e idade.
funcionario = input("Qual seu nome?")
 
genero = input("Qual gênero você se identifica?")

idade = input("Me diga sua idade?")

listaFeminino = ["feminino", "FEMININO", "Feminino"]
listaMasculino = ["masculino", "MASCULINO", "Masculino"]

if genero in listaFeminino:
    if int(idade) > 30:
        print (funcionario + " irá ganhar um kit vermelho!")

    else: 
        print (funcionario + " irá ganhar um kit amarelo!")

if genero in listaMasculino:
    print (funcionario + " irá ganhar um kit preto!")