# multiply two n-digit non-negative integers recursively
# assuming n is a power of 2, integers of equal length

def RecIntMul(x, y):
    x,y = str(x), str(y)
    midpoint = len(x) // 2
    n = len(x)
    if n == 1:
        return int(x)*int(y)
    else:
        a = int(x[:midpoint])
        b = int(x[midpoint:])
        c = int(y[:midpoint])
        d = int(y[midpoint:])
        ac = RecIntMul(a,c)
        ad = RecIntMul(a,d)
        bc = RecIntMul(b,c)
        bd = RecIntMul(b,d)
        return int(10**n * ac + (10**(n/2))*(ad + bc) + bd)

if __name__ == '__main__':
    res = RecIntMul(31415876, 27182818)
    print("Result " + str(res))
 #   print(("Expectation " + str(31415876*27182818)))
