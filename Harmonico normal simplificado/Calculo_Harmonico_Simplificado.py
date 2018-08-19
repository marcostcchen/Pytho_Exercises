def harmonico(n):
    "int -> int e int retorna NUM e DEN"
    NUM, DEN = 0,1
    for i in range(1,n+1):
        NUM, DEN = soma_fracoes(NUM, DEN, 1, i)
    return NUM, DEN

def soma_fracoes(n1, d1, n2, d2):
    DEN = d1*d2
    NUM = n1*d2 + n2*d1
    return simplifique(NUM, DEN)

def simplifique(NUM, DEN):
    m = mdc(NUM, DEN)
    NUM = NUM//m
    DEN = DEN//m
    return NUM,DEN

def mdc(NUM, DEN):
    d = min(NUM,DEN)
    while NUM%d !=0 or DEN%d !=0:
        d = d-1
    return d

n = int(input("Digite n:"))
num,den = harmonico(n)
print("1+1/2+...+1/%d = %d / %d"%(n,num,den))