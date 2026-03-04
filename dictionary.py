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
                    return valore[1]
                else:
                    return t.handleTranslate(valore)

    def translateWordWildCard(self):
        pass
