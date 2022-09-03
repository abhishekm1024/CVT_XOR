import numpy as np
from PIL import Image
array = np.zeros([1000, 1000, 3], dtype=np.uint8)


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


# Randomly taking two matrix A and B with entries 0 to 1000
random_matrix_A = np.random.randint(1000, size=(1000, 1000))
print("matrix-'A'")
print(random_matrix_A)
random_matrix_B = np.random.randint(1000, size=(1000, 1000))
print("matrix-'B'")
print(random_matrix_B)
matrix_CVT = np.random.randint(1, size=(1000, 1000))
matrix_XOR = np.random.randint(1, size=(1000, 1000))
for i in range(1000):
    for j in range(1000):
        matrix_CVT[i][j] = convert_cvt(random_matrix_A[i][j], random_matrix_B[i][j])
img = Image.fromarray(matrix_CVT)
img.show("matrix_CVT.png")
for i in range(1000):
    for j in range(1000):
        matrix_XOR[i][j] = convert_xor(random_matrix_A[i][j], random_matrix_B[i][j])
img = Image.fromarray(matrix_XOR)
img.show("matrix_Xor.png")