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
            d.addWord(txt, dizionario, lista)
            print("Aggiunta!\n")

    if int(txtIn) == 2:
        print()
        txt = input("Ok, quale parola devo cercare? ").lower()
        if txt.isalpha():
            elemento = d.translate(txt)
            print(elemento, "\n")

    if int(txtIn) == 3:
        pass

    if int(txtIn) == 4:
        # alternativa: for el in lista:

        infile = open("dictionary.txt", "r", encoding="utf-8")
        lines = infile.readlines()
        for i in range(0, len(lines)):
            lines[i] = lines[i].strip("\n")
            valore = lines[i].split()
            for j in range(0, len(valore)):
                print(valore[j], end=" ")
            print()

    if int(txtIn) == 5:
        break