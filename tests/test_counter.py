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

	def _check(self, counter, base, values):
		assert counter.base == base
		assert set(counter) == set(values), (set(counter), set(values))

		for key, value in values.iteritems():
			assert counter[key] == value, (key, value, counter[key])

	def test_ops_counter(self):
		c = prob.Counter(0.0)
		c['a'] = 1.0
		c['b'] = 2.0

		o = prob.Counter(0.5)
		o['a'] = 0.1

		r = c + o
		self._check(r, 0.5, {'a': 1.1, 'b': 2.5})
		r = c * o
		self._check(r, 0.0, {'a': 0.1, 'b': 1.0})
		r = c / o
		self._check(r, 0.0, {'a': 10.0, 'b': 4.0})

	def test_iops_counter(self):
		c = prob.Counter(0.0)
		c['a'] = 1.0
		c['b'] = 2.0

		o = prob.Counter(0.5)
		o['a'] = 0.1

		r = c.copy()
		r += o
		self._check(r, 0.5, {'a': 1.1, 'b': 2.5})

		r = c.copy()
		r *= o
		self._check(r, 0.0, {'a': 0.1, 'b': 1.0})

		r = c.copy()
		r /= o
		self._check(r, 0.0, {'a': 10.0, 'b': 4.0})

	def test_ops_number(self):
		c = prob.Counter(0.0)
		c['a'] = 1.0
		c['b'] = 2.0

		o = 0.5

		r = c + o
		self._check(r, 0.5, {'a': 1.5, 'b': 2.5})
		r = c * o
		self._check(r, 0.0, {'a': 0.5, 'b': 1.0})
		r = c / o
		self._check(r, 0.0, {'a': 2.0, 'b': 4.0})

	def test_iops_number(self):
		c = prob.Counter(0.0)
		c['a'] = 1.0
		c['b'] = 2.0

		o = 0.5

		r = c.copy()
		r += o
		self._check(r, 0.5, {'a': 1.5, 'b': 2.5})

		r = c.copy()
		r *= o
		self._check(r, 0.0, {'a': 0.5, 'b': 1.0})

		r = c.copy()
		r /= o
		self._check(r, 0.0, {'a': 2.0, 'b': 4.0})


if __name__ == "__main__":
	unittest.main()
