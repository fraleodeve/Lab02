class Translator:

    def __init__(self, parola_aliena = "a", parola_umana = "a"):
        self.parola_aliena = parola_aliena
        self.parola_umana = parola_umana

    def printMenu(self):
        print("---------------------------------")
        print("Translator Alien-Italian\n")
        print("---------------------------------")
        print("1. Aggiungi una nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")
        print("---------------------------------\n")


    def loadDictionary(self, dict):
        infile = open(dict, "r", encoding="utf-8")
        lines = infile.readlines()
        lista = list()
        for i in range(0, len(lines)):
            lines[i] = lines[i].strip("\n")
            valore = lines[i].split()
            elemento = Translator(valore[0], valore[1])
            lista.append(elemento)
        return lista
        # dict is a string with the filename of the dictionary

    def handleAdd(self, entry, d, lista):
        valore = entry.split()
        posizione = 0

        for i in range(0, len(lista)):
            if lista[i].parola_aliena == valore[0]:
                posizione = i

        file = open("dictionary.txt", "r", encoding="utf-8")
        righe = file.readlines()
        for i in range(1, len(valore)):
            righe[posizione] = righe[posizione].rstrip("\n") + " " + valore[i] + "\n"

        file.close()
        file = open("dictionary.txt", "w", encoding="utf-8")
        file.writelines(righe)
        file.close()
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>

    def handleTranslate(self, query):
        risultato = ""
        for i in range (1, len(query)):
            risultato = risultato + query[i] + " "
        # query is a string <parola_aliena>
        return risultato

    def handleWildCard(self,query):
        risultato = ""
        for i in range(1, len(query)):
            risultato = risultato + query[i] + " "
        # query is a string with a ? --> <par?la_aliena>
        return risultato