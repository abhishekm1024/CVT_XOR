def binary(x):     # from decimal to binary
    return int(bin(x)[2:])


def decimal(x):     # from binary to decimal
    return int(str(x), 2)


def convert_xor(x, y):               # converting numbers in XOR
    a = binary(x)
    b = binary(y)
    c = "0"
    while a > 0 and b > 0:
        if (a % 2 == 1 and b % 2 == 1) or (a % 2 == 0 and b % 2 == 0):
            c = "0" + c
        else:
            c = "1" + c
        a = a // 10
        b = b // 10
    c = int(c) // 10              # removing 0 from end
    return decimal(c)
