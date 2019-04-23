class Vector(object):
  """linear algebra intro"""
  def __init__(self, *coordinates):
    try:
      if not coordinates:
          raise ValueError
      self.coordinates = coordinates
      self.dimensions = len(coordinates)
    except ValueError:
        raise ValueError('The coordinates must be nonempty')
    except TypeError:
        raise TypeError('The coordinates must be iterable')

  def __iter__(self):
      return self.coordinates.__iter__()

  def __str__(self):
    return 'Vector{}'.format(self.coordinates)

  def __eq__(self, other):
    return self.coordinates == other.coordinates

  def __rmul__(self, other):
      return self.__mul__(other)

  def __mul__(self, other):
    if type(other) == type(1) or type(other) == type(1.0):
        p = tuple(x*other for x in self.coordinates)
        return Vector(*p)

  def __sub__(self, other):
    p = tuple(x - y for x, y  in zip(self, other))
    return Vector(*p)

  def __add__(self, other):
    p = tuple(x + y for x, y  in zip(self, other))
    return Vector(*p)

  __repr__ = __str__

import unittest

class QuizOne(unittest.TestCase):
      def test_addition(self):
          x =  Vector(8.218, -9.341)
          y = Vector(-1.129, 2.111)
          self.assertEqual(x + y, Vector(7.089, -7.229999999999999)) # ✔

      def test_subtraction(self):
          x = Vector(7.119, 8.215)
          y = Vector(-8.223, 0.878)
          self.assertEqual(x-y, Vector(15.342, 7.337)) # ✔

      def test_scalar_multiplication(self):
          x = Vector(1.671,-1.012,-0.318)
          self.assertEqual(x*7.41, Vector(12.38211, -7.49892, -2.35638)) # ✔

if __name__ == "__main__":
    unittest.main()