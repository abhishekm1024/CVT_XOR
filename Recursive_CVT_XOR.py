def binary(x):     # from decimal to binary
    return int(bin(x)[2:])

def decimal(x):     # from binary to decimal
    return int(str(x), 2)

def isZero(x):
    for row in x:
        for i in row:
            if i !=0:
                return False
    return True        
            
def cvt(x, y):               # converting numbers in CVT
    return (x&y)<<1

def xor(x, y):               # converting numbers in XOR
    return x^y

def cvt_m(x, y):
    res = np.zeros((n,m), dtype = np.int64)
    for i in range(n):
        for j in range(m):
            res[i][j] = cvt(x[i][j], y[i][j])
    return res        
                       
def xor_m(x, y):
    res = np.zeros((n,m), dtype = np.int64)
    for i in range(n):
        for j in range(m):
            res[i][j] = xor(x[i][j], y[i][j])    
    return res

class Recursive_CVT_XOR:
    def __init__(self):
      self.result = None

    def solve(self, x, y):
        if isZero(x):
            self.result = [x, y]
        elif isZero(y):
            self.result = [y, x]
        else:
            cvt = cvt_m(x, y)
            xor = xor_m(x, y)
            self.solve(cvt, xor)
			
n = 2
m = 2
A = np.random.randint(1000, size=(n, m))
B = np.random.randint(1000, size=(n, m))

action = Recursive_CVT_XOR()
action.solve(A, B)

print(action.result)