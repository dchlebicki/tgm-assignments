class Bruch(object):
    """
    Holds a fraction and allows special operations by using function/operator overloading

    :ivar int z: the numerator
    :ivar int n: the denominator
    """
    def __init__(self, z, n=1):
        """
        Initializes a fraction
        Bruch(2, 3) -> 2/3
        Bruch(4) -> 4/1

        :param z: the numerator
        :param n: the denominator
        :raises: TypeError, ZeroDivisionError
        """
        # checking conditions
        if type(z) is str or type(n) is str:
            raise TypeError
        elif type(z) is float or type(n) is float:
            # some parts of the code are compatible with float values by default
            # this condition exists to trigger the testcreateBruchWrongTypeNenner
            # and testcreateBruchWrongTypeZaehler test functions positively
            raise TypeError
        elif n == 0:
            raise ZeroDivisionError

        self.z = z
        self.n = n

    def __add__(self, other):
        """
        + (add) operator overload, used in cases like:
        Bruch(1, 2) + Bruch(3, 4)
        Bruch(2, 3) + 1

        :param other: Bruch, int, float
        :return: int, float
        :raises: TypeError
        """
        if type(other) is str or type(other) is float:
            raise TypeError
        elif type(other) is Bruch:
            return self.z/self.n + other.z/other.n
        else:
            return self.z/self.n + other

    def __iadd__(self, other):
        """
        += (add) operator overload, used in cases like:
        bruch += 1
        bruch += Bruch(2, 3)

        :param other: Bruch, int, float
        :return: Bruch
        :raises: TypeError
        """
        if type(other) is str:
            raise TypeError
        elif type(other) is Bruch:
            z = self.z * other.n + other.z * self.n
            n = self.n * other.n
            return Bruch(z, n)
        else:
            z = self.z + other * self.n
            return Bruch(z, self.n)

    def __radd__(self, other):
        """
        right-hand + (add) operator overload, used in cases like:
        1 + Bruch(1, 2)

        :param other: Bruch, int, float
        :return: int, float
        :raises: TypeError
        """
        return self + other # using .__add__ function

    def __sub__(self, other):
        """"
        - (subtract) operator overload, used in cases like:
        Bruch(1, 2) - Bruch(3, 4)
        Bruch(2, 3) - 1

        :param other: Bruch, int, float
        :return: int, float
        :raises: TypeError
        """
        if type(other) is str:
            raise TypeError
        elif type(other) is Bruch:
            return self.z/self.n - other.z/other.n
        else:
            return self.z/self.n - other

    def __isub__(self, other):
        """
        -= (subtract) operator overload, used in cases like:
        bruch -= 1
        bruch -= Bruch(2, 3)

        :param other: Bruch, int, float
        :return: Bruch
        :raises: TypeError
        """
        if type(other) is str:
            raise TypeError
        elif type(other) is Bruch:
            z = self.z * other.n - other.z * self.n
            n = self.n * other.n
            return Bruch(z, n)
        else:
            z = self.z - other * self.n
            return Bruch(z, self.n)

    def __rsub__(self, other):
        """
        right-hand - (subtract) operator overload, used in cases like:
        1 - Bruch(1, 2)

        :param other: Bruch, int, float
        :return: int, float
        :raises: TypeError
        """
        # using .__sub__ function,
        # float() is needed to prevent infinite loop (self execution)
        if type(other) is str or type(other) is float:
            raise TypeError
        return other - float(self)

    def __mul__(self, other):
        """
        * (multiply) operator overload, used in cases like:
        Bruch(1, 2) * 2
        Bruch(1, 4) * Bruch(2)

        :param other: Bruch, int, float
        :return: int, float
        :raises: TypeError
        """
        if type(other) is str or type(other) is float:
            raise TypeError
        elif type(other) is Bruch:
            return (self.z * float(other.z)) / (self.n * float(other.n))
        else:
            return (self.z * other) / self.n

    def __imul__(self, other):
        """
        += (multiply) operator overload, used in cases like:
        bruch *= 2
        bruch *= Bruch(3, 2)

        :param other: Bruch, int, float
        :return: Bruch
        :raises: TypeError
        """
        if type(other) is str:
            raise TypeError
        elif type(other) is Bruch:
            return self * other
        else:
            return self * other

    def __rmul__(self, other):
        """
        right-hand * (multiply) operator overload, used in cases like:
        2 * Bruch(1, 2) = 1

        :param other: Bruch, int, float
        :return: int, float
        :raises: TypeError
        """
        # see line 22, float excluded to trigger testMulError positively
        if type(other) is str or type(other) is float:
            raise TypeError
        elif type(other) is Bruch:
            return (self.z * float(other.z)) / (self.n * float(other.n))
        else:
            return (self.z * other) / self.n

    def __truediv__(self, other):
        """
        / (divide) operator overload, used in cases like:
        Bruch(1, 2) / 2
        Bruch(3, 2) / Bruch(3, 1)

        :param other: Bruch, int, float
        :return: int, float
        :raises: TypeError, ZeroDivisionError
        """
        if type(other) is str or type(other) is float:
            raise TypeError
        elif float(other) == 0:
            raise ZeroDivisionError
        elif type(other) is Bruch:
            return (self.z / self.n) * (float(other.n) / float(other.z))
        else:
            return (self.z / self.n) / other

    def __itruediv__(self, other):
        """
        /= (divide) operator overload

        :param other: Bruch, int, float
        :return: Bruch
        :raises: TypeError, ZeroDivisionError
        """
        if type(other) is str or type(other) is float:
            raise TypeError
        if type(other) is int:
            if other == 0:
                raise ZeroDivisionError
            else:
                return Bruch(self.z, self.n * other)
        elif type(other) is Bruch:
            return self.__truediv__(other)

    def __rtruediv__(self, other):
        """
        right-hand / (divide) operator overload, used in cases like:
        4 / Bruch(2, 1)

        :param other: Bruch, int, float
        :return: int, float
        :raises: TypeError, ZeroDivisionErrorer
        """
        if type(other) is str or type(other) is float:
            raise TypeError
        elif self.z == 0:
            raise ZeroDivisionError

        return self.__itruediv__(other)

    def __abs__(self):
        """
        returns a positive fraction when using Python's abs() function, used in cases like:
        abs(Bruch(-3, 2)) -> Bruch(3, 2)

        :return: Bruch
        """
        return Bruch(abs(self.z), abs(self.n))

    def __float__(self):
        """
        returns the float value of a fraction, used in cases like:
        float(Bruch(1, 4)) -> 0.25

        :return: float
        """
        return float(self.z / self.n)

    def __int__(self):
        """
        returns the int value of a fraction, used in cases like:
        int(6, 2) -> 3

        :return: int
        """
        return int(self.z / self.n)

    def __str__(self):
        """
        returns the fraction as a well formatted string, used in cases like:
        str(Bruch(2, 3)) -> "(2/3)"
        str(Bruch(3) -> "(3)"

        :return: str
        """
        if self.n == 1:
            return "(" + str(self.z) + ")"
        elif self.z < 0 and self.n < 0: # if (-3/-2)
            return "(" + str(abs(self.z)) + "/" + str(abs(self.n)) + ")"
        else:
            return "(" + str(self.z) + "/" + str(self.n) + ")"

    def __invert__(self):
        """
        inverts the numerator and denominator, used in cases like:
        ~Bruch(4, 2) -> Bruch(2, 4)

        :return: Bruch
        """
        return Bruch(self.n, self.z)

    def __iter__(self):
        """
        returns the numerator and the denominator as a tuple

        :return: tuple?
        """
        yield self.z
        yield self.n

    def __eq__(self, other):
        """
        == (equals) operator overload, checks if fractions are equal to each other, used in cases like:
        Bruch(2, 3) == Bruch(2, 3) -> True
        Bruch(1, 3) == Bruch(2, 6) -> True
        Bruch(1, 4) == Bruch(1, 2) -> False

        :param other: Bruch
        :return: boolean
        :raises: TypeError
        """
        if type(other) is not Bruch:
            raise TypeError
        elif self.z / self.n == float(other.z) / float(other.n):
            return True
        else:
            return False