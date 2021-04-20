class Complex:

    def __init__(self, cifra1, cifra2):
        self.cifra1 = cifra1
        self.cifra2 = cifra2

    def __add__(self, other):
        _sum_ = self.cifra1 + other.cifra2

    def __sub__(self, other):
        _sub_ = self.cifra1 - other.cifra2

    def __mul__(self, other):
        _mul_ = self.cifra1 * other.cifra2

    def __truediv__(self, other):
        _div_ = self.cifra1 / other.cifra2


a = complex(input('Ввод1:'))
b = complex(input('Ввод2:'))
Complex3 = a * b

print(Complex3)

#2
class Complex0:

    def __init__(self, cifra1, cifra2):
        self.cifra1 = cifra1
        self.cifra2 = cifra2

    def __add__(self, other):
        cifra1 = self.cifra1 * other.cifra2 + self.cifra1 * other.cifra2
        cifra2 = self.cifra2 * other.cifra2
        return Complex0(cifra1, cifra2)

Complex1 = complex(4, 6)
Complex2 = complex(4, 10)
Complex3 = Complex1 + Complex2
print(Complex3)

# 3) __str__

class String:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Man - {self.name}"

String1 = String("Mersedes")
print(String1)