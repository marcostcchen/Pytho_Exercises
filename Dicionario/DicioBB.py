class Dicionario:
    '''
    Self.key é o valor da chave
    Self.Values é o numero de repticao da chave
    '''
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
        '''
        :param chave: chave a ser procurada
        :return: Achou, indice
        '''
        ini, fim = 0, len(self.key)
        while ini < fim:
            meio = (ini + fim)//2
            if self.key[meio] == chave:
                return True, meio
            elif self.key[meio] < chave:
                ini = meio + 1
            else:
                fim = meio
        return False, ini

    def get(self,chave):
        achou, i = self.indice(chave)
        if achou:
            return self.values[i]
        return None

    def put(self, chave, valor):
        achou, i = self.indice(chave)
        if achou:
            self.values[i] = valor
        else:
            self.key.append(0)
            self.values.append(0)
            for j in range(len(self.key) - 2, i, -1):
                self.key[j + 1] = self.key[j]
                self.values[j + 1] = self.values[j]
            self.key[i] = chave
            self.values[i] = valor

def main():
    lst_pal = '30 33 40 55 55 60 60 66 70 88'
    dicio = Dicionario(lst_pal)
    dicio.put('20', 1)
    dicio.put('10',1)
    dicio.put('64',1)

    print(dicio)

if __name__ == "__main__":
    main()