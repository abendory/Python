# Recursive approach -- O(n^2)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


# Cached approach -- O(n)
def fib_c(n, f):
    print(f)
    if f[n] == 'UNKNOWN':
        f[n] = fib_c(n-1, f) + fib_c(n-2, f)

    return f[n]


def fib_c_driver(n):
    f = []
    f.append(0)
    f.append(1)
    for i in range(n+1):
        f.append('UNKNOWN')  # initialize

    return fib_c(n, f)


# Dynamic Programming approach -- O(n)
def fib_dp(n):
    f = ["x"] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, len(f)):
        f[i] = (f[i-1]+f[i-2])

    return f[n]


def fib_ultimate(n):
    back2 = 0   # n = 0
    back1 = 1   # n = 1

    if n == 0: return 0

    for i in range(2,n):
        next_num = back1+back2
        back2 = back1
        back1 = next_num
    return back1 + back2

print fib_ultimate(1000)
