import translator as tr

t = tr.Translator()

class Dictionary:
    def __init__(self, parola_aliena = "a", parola_umana = "a"):
        self.parola_aliena = parola_aliena
        self.parola_umana = parola_umana


    def addWord(self, txtIn, d):
        valore = txtIn.split()
        count = 0
        for (key, val) in d.items():
            if key == valore[0]:
                count = 1
        if len(valore) == 2 and count == 0:
            elemento = Dictionary(valore[0], valore[1])
        else:
            elemento = t.handleAdd(txtIn, d)
        return elemento

    def translate(self, txt, lista):
        for el in lista:
            if el.parola_aliena == txt:
                return el.parola_umana

    def translateWordWildCard(self):
        pass
