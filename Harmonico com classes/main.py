from fracao import Fracao

def simplifique(x):
    d = min(x.num,x.den)
    while x.num%d != 0 or x.den%d !=0 :
        d = d-1
    x.num = x.num//d
    x.den = x.den//d
    return x

def harmonico(n):
    soma = Fracao()
    for i in range(1,n+1):
        soma += Fracao(1,i)
    return simplifique(soma)

n = int(input('Digite n:'))
hn = harmonico(n)
print("1 + 1/2 + 1/3 +...+ 1/%d = "%(n), hn)