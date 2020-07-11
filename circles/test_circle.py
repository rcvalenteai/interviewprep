import unittest
from circles import Circle
from math import pi


class CircleTest(unittest.TestCase):
    def test_circle_area_int(self):
        # Test Area function accuracy with integers
        self.assertAlmostEqual(Circle(1).area(), pi)
        self.assertAlmostEqual(Circle(5).area(), 5**2 * pi)

    def test_circle_area_float(self):
        # Test float calculation of area
        self.assertAlmostEqual(Circle(5.5).area(), 5.5**2 * pi)
        self.assertAlmostEqual(Circle(5.98).area(), 5.98**2 * pi)

    def test_circle_validation(self):
        # Test radius(r) validation
        # Test string
        self.assertRaises(ValueError, Circle, "hi")
        # Test object input
        self.assertRaises(ValueError, Circle, Circle(5))
        # Test negative
        self.assertRaises(ValueError, Circle, -5)
        # Test complex
        self.assertRaises(ValueError, Circle, 5j)

    def test_circle_perimeter(self):
        # Test circle perimeter calculation
        self.assertAlmostEqual(Circle(5).perimeter(), 2 * pi * 5)
        self.assertAlmostEqual(Circle(1).perimeter(), 2 * pi)
        self.assertAlmostEqual(Circle(1.52).perimeter(), 2 * pi * 1.52)

    def test_circle_diameter(self):
        # Test circle perimeter calculation
        self.assertAlmostEqual(Circle(3).diameter(), 2 * 3)
        self.assertAlmostEqual(Circle(1).diameter(), 2)
        self.assertAlmostEqual(Circle(4.57).diameter(), 2 * 4.57)


if __name__ == '__main__':
    unittest.main()
