def binary(x):     # from decimal to binary
    return int(bin(x)[2:])


def decimal(x):     # from binary to decimal
    return int(str(x), 2)


def convert_cvt(x, y):               # converting numbers in CVT
    a = binary(x)
    b = binary(y)
    c = "0"
    while a > 0 and b > 0:
        if a % 2 == 1 and b % 2 == 1:
            c = "1" + c
        else:
            c = "0" + c
        a = a // 10
        b = b // 10
    return decimal(int(c))
