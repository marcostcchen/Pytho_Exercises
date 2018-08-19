def bem_formada(s):
    '''(Str) -> Bool'''
    p = []
    n = len(s)
    for i in range(n):
        if s[i] != '{' and s[i] != '[' and s[i] != '(' and s[i] != '}' and s[i] != ']' and s[i] != ')':
            return False
        if s[i] == '{' or s[i] == '[' or s[i] == '(':
            p.append(s[i])
        if s[i] == '}' or s[i] == ']' or s[i] == ')':
            p_ultimo = p.pop()
            if p_ultimo == '{' and s[i] != '}':
                return False
            if p_ultimo == '[' and s[i] != ']':
                return False
            if p_ultimo == '(' and s[i] != ')':
                return False
    if p != []:
        return False
    return True

def main():
    s = str(input("Digite uma string: "))
    r = bem_formada(s)
    if r == True:
        print("Bem formada!")
    elif r == False:
        print("Mal formada")

if __name__ == "__main__":
    main()