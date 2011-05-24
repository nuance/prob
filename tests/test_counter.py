import unittest

import prob

class CounterTest(unittest.TestCase):
	def test_missing(self):
		c = prob.Counter(0.0)
		assert c['k'] == 0.0

		c = prob.Counter(0.5)
		assert c['k'] == 0.5

	def test_copy(self):
		c = prob.Counter(0.5)
		c['a'] = 1.0
		c['b'] = 2.0

		d = c.copy()
		assert d['a'] == 1.0
		assert d['b'] == 2.0
		assert d[''] == 0.5

	def test_apply(self):
		c = prob.Counter(0.0)
		c.apply(lambda k, v: 1.0)

		assert c[''] == 1.0

		c = prob.Counter(1.0)
		c['a'] = 0.0
		c.apply(lambda k, v: v * 2)

		assert c[''] == 2.0
		assert c['a'] == 0.0

	def test_apply_with_keys(self):
		c = prob.Counter(2.0)
		c['a'] = 0.0
		c.apply(lambda k, v: v + 1.0, ['a', 'b'])

		assert c['a'] == 1.0
		assert c['b'] == 3.0

	def test_normalize(self):
		c = prob.Counter(0.0)
		c.normalize()
		assert c[''] == 0.0

		c = prob.Counter(1.0)
		c.normalize(base_mass=0.5)
		assert c[''] == 2.0

		c = prob.Counter(0.0)
		c['a'] = 1.0
		c['b'] = 3.0

		c.normalize()
		assert c['a'] == 0.25
		assert c['b'] == 0.75

	def test_inner_product(self):
		c = prob.Counter(0.0)
		o = prob.Counter(0.0)

		c['a'] = 1.0
		c['b'] = 4.0

		o['a'] = 3.0
		o['b'] = 1.0

		assert c.inner_product(o) == 7.0


if __name__ == "__main__":
	unittest.main()
