

class QuantityError(Exception):

	def __init__(self, msg: str):
		self.msg = msg

	def __str__(self) -> str:
		return self.msg


class PrefixError(QuantityError, KeyError):
	def __init__(self, msg: str):
		QuantityError.__init__(self, msg)
		KeyError.__init__(self)