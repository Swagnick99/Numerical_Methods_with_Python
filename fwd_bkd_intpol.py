import math

def decimals(s):
    i = 0
    n = len(s)
    while (i < n) and (s[i] != '.'):
        i += 1
    return len(s[i+1:])

print("Number of data points: ", end="")
n = int(input())

print("Enter values of x: ", end="")
x = list(map(float, input().split()))

print("Enter values of f(x): ", end="")
dfx = []
fx = list(input().split())
dec = max(decimals(fx[0]), 3)
fx = [float(x) for x in fx]
dfx.append(fx)

for i in range(1, n):
    fx = []
    for j in range(n-i):
        fx.append(round(dfx[i-1][j+1]-dfx[i-1][j], dec))
    dfx.append(fx)

for i in range(n):
    print(dfx[i])

h = x[1] - x[0]
print("h: {}".format(h))
val = float(input("What x you want f(x) for? "))
fwd_diff = val - x[0]
bkd_diff = x[n-1] - val

if fwd_diff < bkd_diff:
    s = (val-x[0]) / h
    print("s: {}".format(s))

    f = dfx[0][0]
    for i in range(1, n):
        tmp = 1
        for j in range(i):
            tmp *= s-j
        tmp *= dfx[i][0]
        f += tmp / math.factorial(i)
    print("Ans: ", end="")
    print(round(f, dec))
else:
    s = (val-x[n-1]) / h
    print("s: {}".format(s))

    f = dfx[0][n-1]
    for i in range(1, n):
        tmp = 1
        for j in range(i):
            tmp *= s+j
        tmp *= dfx[i][n-i-1]
        f += tmp / math.factorial(i)
    print("Ans: ", end="")
    print(round(f, dec))