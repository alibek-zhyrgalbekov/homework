class Fraction:
    def __init__(self, num, denum):
        self.num = num
        if denum == 0:
            raise ValueError("Can't 0!")
        self.denum = denum

    def add(self, other):
        num = self.num * other.denum + other.num * self.denum
        denum = self.denum * other.denum
        print(num)
        print("-")
        print(denum)

    def div(self, other):
        num = self.num * other.denum
        denum = self.denum * other.num
        print(num)
        print("-")
        print(denum)

    def mul(self, other):
        num = self.num * other.num
        denum = self.denum * other.denum
        print(num)
        print("-")
        print(denum)


fraction1 = Fraction(1, 2)
fraction2 = Fraction(1, 8)
fraction1.mul(fraction2)
