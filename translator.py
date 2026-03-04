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

    def handleAdd(self, entry, d):
        valore = entry.split()
        count = 0
        for (key, val) in d.items():
            if key == valore[0]:
                count = 1
        if count == 1:
            for (key, val) in d.items():
                if key == valore[0]:
                    val.append(valore[1])
                    return Translator(key, valore[0] + " " + valore[1])
        # aggiornare precedente non aggiungerlo

        if (len(valore)) != 2:
            for i in range(1, len(valore)-1):
                for (key, val) in d.items():
                    if key == valore[0]:
                        val.append(valore[i])
        return Translator(valore[0], valore[1]) # cambiare


        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass