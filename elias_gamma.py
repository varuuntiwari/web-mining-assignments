# Program to perform Elias gamma encoding and decoding
# on all even numbers in the range 1 to 20.

from math import log, pow

def getUnary(n):
    return ('0'*n) + '1'

def getBinary(x, n):
    f = '{0:0%db}' % n
    return f.format(x)

def encode(e):
    # Largest power of 2 within limit of e
    n = int(log(e, 2))
    # Remainder left over after largest power removed from e
    b = e - (2 ** (int(log(e, 2))))
    return getUnary(n) + getBinary(b, n)

def decode(d):
    unary = 0
    while d[unary] != '1':
        unary += 1
    
    a = int(pow(2, int(unary)))
    binary = d[int(unary+1):]
    b = int(binary, 2)
    return a + b


encoded = []
# Encoding numbers
print("n\t| encoded n")
print("--------------------")
for e in range(1, 21):
    if e%2 == 0:
        res = encode(e)
        print(f"{e}\t| {res}")
        encoded.append(res)
print()

# Decoding numbers
print("b     \t\t | decoded b")
print("-----------------------------")
for d in encoded:
    print(f"{d}     \t | {decode(d)}")