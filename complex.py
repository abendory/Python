import math

class Complex:
    def __init__(self, real, imag):
        self.r = real
        self.i = imag

    def __repr__(self):
        real = '{0:.2f}'.format(self.r)
        imag = '{0:.2f}'.format(self.i) + 'i'
        if self.i >= 0:
            imag = '+' + imag
        return real + imag

    def __add__(self, a):
        return Complex(self.r + a.r, self.i + a.i)

    def __sub__(self, a):
        return Complex(self.r - a.r, self.i - a.i)

    def __mul__(self, a):
        return Complex(self.r * a.r - self.i * a.i,
                       self.i * a.r + self.r * a.i)

    def __truediv__(self, a):
        top = self * a._conj()
        bottom = a * a._conj()
        real = top.r / bottom.r
        imag = top.i / bottom.r
        return Complex(real, imag)

    def _conj(self):
        return Complex(self.r, -self.i)

def mod(a):
    return Complex(math.sqrt(a.r**2 + a.i**2),0)

A = Complex(1, 4)
B = Complex(2, 5)

print(A)
print(B)
print()
print(A + B)
print(A - B)
print(A * B)
print(A / B)
print(mod(A))
print(mod(B))
