class Dicionario:
    def __init__(self, string):
        self.key = []
        self.values = []
        string = string.split()
        for palavra in string:
            valor = self.get(palavra)
            if valor == None:
                self.put(palavra, 1)
            else:
                self.put(palavra, valor + 1)

    def __str__(self):
        s = ""
        for i in range(len(self.values)):
            s += "%s %d\n"%(self.key[i],self.values[i])
        return s

    def indice(self, chave):
        for i in range(len(self.key)):
            if self.key[i] == chave:
                return i
        return None

    def get(self,chave):
        index = self.indice(chave)
        if index != None:
            return self.values[index]
        return None

    def put(self, chave, valor):
        index = self.indice(chave)
        if index != None:
            self.values[index] = valor
        else:
            self.key.append(chave)
            self.values.append(valor)

def main():
    lst_pal = 'Ola Chen Ola Chen Marcos Tudo Bom Bom Bom BOM '
    dicio = Dicionario(lst_pal)
    print(dicio)



if __name__ == "__main__":
    main()