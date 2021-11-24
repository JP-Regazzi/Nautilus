#2
def conta_bits(n):
    b = str(bin(n))
    return b.count("1")

print(conta_bits(1234))