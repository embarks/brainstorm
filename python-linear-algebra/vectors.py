from math import sqrt, acos
# TODO Decimal

class Vector(object):
  """linear algebra intro"""
  def __init__(self, *coordinates):
    try:
      if not coordinates:
          raise ValueError
      self.coordinates = coordinates
      self.dimensions = len(coordinates)
      self.__magnitude = sqrt(sum([c**2 for c in coordinates]))
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
    elif type(other) == type(self):
        return self.dot(other)

  def __sub__(self, other):
    p = tuple(x - y for x, y  in zip(self, other))
    return Vector(*p)

  def __add__(self, other):
    p = tuple(x + y for x, y  in zip(self, other))
    return Vector(*p)

  def get_magnitude(self):
    return self.__magnitude

  def normalized(self):
    try:
      return (1/self.get_magnitude()) * self
    except ZeroDivisionError:
      raise Exception("Zero vectors do not have a normalization")

  def dot(self, other):
    return sum(x*y for x, y in zip(self, other))

  def theta(self, other):
    u1 = self.normalized()
    u2 = other.normalized()
    return acos(u1.dot(u2))

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

      def test_magnitude(self):
          x = Vector(3, 3, 3)
          y = Vector(-0.221, 7.437)
          z = Vector(8.813, -1.331, -6.247)
          self.assertEqual(5.196152422706632, x.get_magnitude()) # ✔
          self.assertEqual(7.440282924728065, y.get_magnitude()) # ✔
          self.assertEqual(10.884187567292289, z.get_magnitude()) # ✔

      def test_normalization(self):
          x = Vector(1, 1, 1)
          y = Vector(5.581, -2.136)
          z = Vector(1.996, 3.108, -4.554)
          self.assertEqual(Vector(0.5773502691896258, 0.5773502691896258, 0.5773502691896258), x.normalized()) # ✔
          self.assertEqual(Vector(0.9339352140866403, -0.35744232526233), y.normalized()) # ✔
          self.assertEqual(Vector(0.3404012959433014, 0.5300437012984873, -0.7766470449528029), z.normalized()) # ✔

      def test_angle(self):
          v = Vector(3,-7)
          w = Vector(-2, 5)
          self.assertEqual(3.1172072444170658, v.theta(w)) # ✔

          v2 = Vector(7.35, 0.221, 5.188)
          v3 = Vector(2.751, 8.259, 3.985)
          self.assertEqual(1.0520113648417708, v2.theta(v3)) # ✔


      def test_dot(self):
          v = Vector(7.887, 4.138)
          w = Vector(-8.802, 6.776)
          self.assertEqual(-41.382286, v*(w))  # ✔

          v2 = Vector(-5.955, -4.904, -1.874)
          w2 = Vector(-4.496, -8.755, 7.103)
          self.assertEqual(56.397178000000004, v2*w2) # ✔



if __name__ == "__main__":
    unittest.main()