

class QuantityError(Exception):
	"""Base exception class for exceptions of this package"""

	def __init__(self, msg: str):
		self.msg = msg

	def __str__(self) -> str:
		return self.msg


class PrefixError(QuantityError, KeyError):
	"""Subexception of QuantityError
	Exception raise for prefix error.
	"""

	def __init__(self, msg: str):
		QuantityError.__init__(self, msg)
		KeyError.__init__(self)


class NoPrefixSupported(QuantityError):
	"""Subexception of QuantityError
	Exception raise when a prefix method is used for a quantity which not support prefix (Celcius temperature...).
	"""

	def __init__(self):
		QuantityError.__init__(self, "Prefix are not supported for this quantity.")