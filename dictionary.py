import translator as tr

t = tr.Translator()

class Dictionary:
    def __init__(self, parola_aliena = "a", parola_umana = "a"):
        self.parola_aliena = parola_aliena
        self.parola_umana = parola_umana

    def addWord(self, txtIn, d, lista):
        valore = txtIn.split()
        count = 0
        for (key, val) in d.items():
            if key == valore[0]:
                count = 1
        if len(valore) == 2 and count == 0:
            file = open("dictionary.txt", "a")
            file.write("\n" + valore[0] + " " + valore[1])
            file.close()
        else:
            t.handleAdd(txtIn, d, lista)

    def translate(self, txt):
        infile = open("dictionary.txt", "r", encoding="utf-8")
        lines = infile.readlines()
        lista = list()
        for i in range(0, len(lines)):
            lines[i] = lines[i].strip("\n")
            valore = lines[i].split()
            if valore[0] == txt:
                if len(valore) == 2:
                    lista.append(valore[1])
                else:
                    a = t.handleTranslate(valore)
                    lista.append(a)
        return lista

    def translateWordWildCard(self, tx):
        infile = open("dictionary.txt", "r", encoding="utf-8")
        lines = infile.readlines()
        posizione = 0
        lista = list()
        for i in range (0, len(tx)):
            if tx[i] == "?":
                posizione = i

        for i in range(0, len(lines)):
            lines[i] = lines[i].strip("\n")
            valore = lines[i].split()
            if posizione == 0:
                if valore[0][posizione:] == tx[posizione:]:
                    if len(valore) == 2:
                        lista.append(valore[1])
                    else:
                        a = t.handleTranslate(valore)
                        lista.append(a)

            if valore[0][:posizione] == tx[:posizione] and valore[0][posizione+1:] == tx[posizione+1:]:
                if len(valore) == 2:
                    lista.append(valore[1])
                else:
                    c = t.handleTranslate(valore)
                    lista.append(c)
        return lista
