# Entregável - Python Basico 

#1
def pg_pa(n1, nx, r):
    if (type(n1) == type(nx) == type(r) == int):
        l = []
        if (r%2 == 0):
            while n1 <= nx:
                l.append(n1)
                n1 += r
        else:
            while n1 <= nx:
                l.append(n1)
                n1 = n1 * r
        return l
    else:
        return "A função só trabalha com valores inteiros!"

# Exemplos de uso da função 
print(pg_pa(2,13,4))
print(pg_pa(2,13,3))