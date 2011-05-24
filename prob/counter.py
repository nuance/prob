import math

# A constant denoting the default value, for use in the apply methods
DEFAULT = {}

def _log(x):
	"""Python is stupid sometimes"""
	if x == 0.0:
		return float("-inf")
	else:
		return math.log(x)

class Counter(dict):
	"""Store counts and work with them like you would a probability
	distribution.
	"""

	def __init__(self, base, *args):
		super(Counter, self).__init__(*args)

		self.base = float(base)

	def __missing__(self, key):
		self[key] = self.base

		return self.base

	def copy(self):
		r = self.__class__(self.base)

		for k, v in self.iteritems():
			r[k] = v

		return r

	def apply(self, func, keys=None):
		if keys is None:
			keys = self.iterkeys()

		for k in keys:
			self[k] = func(k, self[k])
		self.base = func(DEFAULT, self.base)

	def log(self):
		self.apply(lambda _, value: _log(value))

	def exp(self):
		self.apply(lambda _, value: math.exp(value))

	def normalize(self, base_mass=0.0):
		count = sum(self.itervalues()) + base_mass * self.base

		if count == 0.0:
			return

		self.apply(lambda _, value: value / count)

	@classmethod
	def _keys(cls, a, b):
		keys = set(a)
		keys.update(b)

		return keys

	def _iop(self, other, operation):
		"""Generic in-place operation"""
		if isinstance(other, (int, long, float)):
			self.apply(lambda _, value: operation(value, other))
		else:
			self.apply(lambda key, value: operation(value, other[key]), self._keys(self, other))

	def __iadd__(self, other):
		self._iop(other, lambda a, b: a + b)

	def __imul__(self, other):
		self._iop(other, lambda a, b: a * b)

	def _op(self, other, operation):
		result = self.copy()
		result._iop(other, operation)
		return result

	def __add__(self, other):
		return self._op(other, lambda a, b: a + b)

	def __mul__(self, other):
		return self._op(other, lambda a, b: a * b)

	def __radd__(self, other):
		return self + other

	def __rmul__(self, other):
		return self * other

	def __pow__(self, power, modulo=None):
		result = self.copy()

		result.apply(lambda _, value: value ** power)

		return result

	def inner_product(self, other):
		return sum(self[key] * other[key] for key in self._keys(self, other))
