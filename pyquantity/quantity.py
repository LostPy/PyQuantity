from typing import Union

from . import Unit


class Quantity:
	_unit = None  # define the units of quantity

	def __init__(self, value: float, unit: Union[str, Unit], base_prefix: ):
		"""Initialize an instance of Quantity
	
		Parameters
		----------
		None
		"""
		self._real: float = value  # The value in the base prefix
		self.unit = unit

	def __repr__(self) -> str:
		return f"{self.name}: {self._format_real_value()} {self.unit.symbol}"

	def __str__(self) -> str:
		return f"{self._format_real_value()} {self.unit.symbol}"

	def __format__(self, fmt_spec: str = "") -> str:
		return format(str(self), format_spec=fmt_spec)

	def _format_real_value(self) -> str:
		if abs(self._real) >= 1000:
			return f"{self._real:.3e}"
		return f"{self._real:.3f}"

	@classmethod
	def get_name(cls) -> str:
		return cls.__name__

	@property
	def unit(self) -> Unit:
		return self._unit

	@setter.unit
	def unit(self, new_unit: Union[str, Unit]):
		if isinstance(new_unit, str):
			self._unit = Unit(new_unit, new_unit)
		elif isinstance(new_unit, Unit):
			self._unit = new_unit
		else:
			raise ValueError(f"'new_unit' must be a string which define the symbol of unit or an instance of Unit, not {type(new_unit)}")

	@property
	def name(self) -> str:
		return self.get_name()
