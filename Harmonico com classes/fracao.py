class Fracao:
    def __init__(self,num = 0,den = 1):
        self.num = num
        self.den = den

    def __str__(self):
        if self.den == 1:
            s = "%d"%self.num
        else:
            s = "%d/%d"%(self.num, self.den)
        return s

    def __add__(self, other):
        num = self.num*other.den + self.den*other.num
        den = self.den*other.den
        return Fracao(num, den)


