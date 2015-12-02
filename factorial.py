def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

x=1
while x <= 80:
    print 'Factorial({}) is '.format(str(x)) + str(factorial(x)); x+=1