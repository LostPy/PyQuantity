

class QuantityError(Exception):

	def __init__(self, msg: str):
		self.msg = msg

	def __repr__(self) -> str:
		return f"<{self.get_name()}: {self.msg}>"

	@classmethod
	def get_name(cls) -> str:
		return cls.__name__

