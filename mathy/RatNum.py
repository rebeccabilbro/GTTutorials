# RatNum.py


class RationalNumber:
    """Any number that can be expressed as the quotient or fraction p/q
    of two integers, p and q, with the denominator q not equal to zero.

    Since q may be equal to 1, every integer is a rational number.

    Addition:        n1/d1 + n2/d2 = (n1*d2 + n2*d1)/(d1*d2)

    Subtraction:     n1/d1 - n2/d2 = (n1*d2 - n2*d1)/(d1*d2)

    Multiplication:  n1/d1 * n2/d2 = (n1*n2)/(d1*d2)

    Division:        (n1/d1) / (n2/d2) = (n1*d2)/(d1*n2)

    """

    def __init__(self, numerator, denominator=1):
        self.n = numerator
        self.d = denominator

    def __str__(self):
        return "%s/%s" % (self.n, self.d)

    __repr__ = __str__


    def __add__(self, other):
        '''Addition'''
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return RationalNumber(n, d)

    def __sub__(self, other):
        '''Subtraction'''
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*d2 - n2*d1, d1*d2)

    def __mul__(self, other):
        '''Multiplication'''
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*n2, d1*d2)

    def __div__(self, other):
        '''Division'''
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n1, d1 = self.n, self.d
        n2, d2 = other.n, other.d
        return RationalNumber(n1*d2, d1*n2)


if __name__ == "__main__":
    x = RationalNumber(1,2)
    y = RationalNumber(3,2)
    print y*x
