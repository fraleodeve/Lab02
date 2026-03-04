import translator as tr
import dictionary as di

t = tr.Translator()
d = di.Dictionary()

while(True):

    t.printMenu()

    lista = t.loadDictionary("dictionary.txt")

    dizionario = dict()
    for el in lista:
        dizionario[el.parola_aliena] = [el.parola_umana]

    txtIn = input()

    if int(txtIn) == 1:
        print()
        txt = input("Ok, quale parola devo aggiungere? ").lower()
        copia = txt
        if copia.replace(" ", "").isalpha():
            elemento = d.addWord(txt, dizionario)
            lista.append(elemento)
            print("Aggiunta!\n")

        for el in lista: # cambiare
            p1 = el.parola_aliena
            p2 = el.parola_umana
            print(p1,p2)

    if int(txtIn) == 2:
        print()
        txt = input("Ok, quale parola devo cercare? ").lower()
        if txt.isalpha():
            elemento = d.translate(txt, lista)
            print(elemento, "\n")

    if int(txtIn) == 3:
        pass

    if int(txtIn) == 4:
        for el in lista:
            p1 = el.parola_aliena
            p2 = el.parola_umana
            print(p1,p2)

    if int(txtIn) == 5:
        break