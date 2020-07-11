from math import pi


class Circle(object):
    def __init__(self, r):
        """
        create a circle
        :param r: radius of circle
        """
        if self.__validate_r(r):
            self.r = r

    @staticmethod
    def __validate_r(r):
        """
        ensure the radius is a valid radius for a circle
        :return: True if value passes, throw exception otherwise
        :exception
        """
        # Make sure not negative
        if type(r) is not int and type(r) is not float:
            raise ValueError("The given object is of type " + str(type(r)), " a int or float is expected")
        elif r < 0:
            raise ValueError("The given value is negative, it must be positive")
        return True

    def area(self):
        """
        find the area of a circle
        :return: area of circle
        :rtype: float
        """
        return pi * (self.r ** 2)

    def perimeter(self):
        """
        find the perimeter of a circle
        :return: perimeter of circle
        :rtype: float
        """
        return 2 * pi * self.r

    def diameter(self):
        """
        find the diameter of a circle
        :return: diameter of circle
        :rtype: float or int
        """
        return 2 * self.r
