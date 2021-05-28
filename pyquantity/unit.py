from collections import namedtuple
from typing import Union, List, Tuple, Generator

from . import errors


Prefix = namedtuple('Prefix', ('name', 'symbol', 'value'))


class PrefixEnum:
	yotta = Prefix('yotta', 'Y', 1e24)
	zetta = Prefix('zetta', 'Z', 1e21)
	exa = Prefix('exa', 'E', 1e18)
	peta = Prefix('peta', 'P', 1e15)
	tera = Prefix('tera', 'T', 1e12)
	giga = Prefix('giga', 'G', 1e9)
	mega = Prefix('mega', 'M', 1e6)
	kilo = Prefix('kilo', 'k', 1e3)
	hecto = Prefix('hecto', 'h', 1e2)
	deca = Prefix('deca', 'da', 1e1)
	none = Prefix('', '', 1e0)
	deci = Prefix('deci', 'd', 1e-1)
	centi = Prefix('centi', 'c', 1e-2)
	mili = Prefix('mili', 'm', 1e-3)
	micro = Prefix('micro', 'u', 1e-6)
	nano = Prefix('nano', 'n', 1e-9)
	pico = Prefix('pico', 'p', 1e-12)
	femto = Prefix('femto', 'f', 1e-15)
	atto = Prefix('atto', 'a', 1e-18)
	zepto = Prefix('zepto', 'z', 1e-21)
	yocto = Prefix('yocto', 'y', 1e-24)

	@classmethod
	def add_prefix(cls, name: str, symbol: str, value: float):
		if not isinstance(name, str):
			raise ValueError(f"'name' must be a str not a '{type(name)}'")
		if not isinstance(symbol, str):
			raise ValueError(f"'symbol' must be a str not a '{type(symbol)}'")
		if not isinstance(value, float):
			raise ValueError(f"'value' must be a float not a '{type(value)}'")
		setattr(cls, name, Prefix(name, symbol, value))

	@classmethod
	def remove_prefix(cls, name: str):
		if not isinstance(name, str):
			raise ValueError(f"'name' must be a str not a '{type(name)}'")
		if name in dir(cls):
			return delattr(cls, name)
		raise errors.PrefixError(f"The prefix '{name}' does not exist")

	@classmethod
	def _get_all_prefix(cls) -> List[Prefix]:
		return [attr_ for attr_ in dir(cls) if isinstance(attr_, Prefix)]

	@classmethod
	def _get_all_symbols(cls) -> Generator:
		return (attr_.symbol for attr_ in dir(cls) if isinstance(attr_, Prefix))

	@classmethod
	def _get_prefix_with_value(cls, value: float) -> Prefix:
		for prefix in cls._get_all_prefix():
			if prefix.value == value:
				return prefix
		raise PrefixError(f"The prefix with value '{value}' does not exist")

	@classmethod
	def _get_prefix_with_symbol(cls, symbol: str) -> Prefix:
		for prefix in cls._get_all_prefix():
			if prefix.symbol == symbol:
				return prefix
			raise PrefixError(f"The prefix symbol '{symbol}' does not exist")

	@classmethod
	def get_prefix(cls, arg: Union[str, float]) -> Prefix:
		if isinstance(arg, str) and arg in dir(PrefixEnum):
			return getattr(cls, arg)

		elif isinstance(arg, str) and arg in cls._get_all_symbols():
			return _get_prefix_with_symbol(arg)

		elif isinstance(arg, float):
			return cls._get_prefix_with_value(arg)

		elif isinstance(arg, str):
			raise errors.PrefixError(f"The prefix name or symbol '{arg}' does not exist")

		raise ValueError(f"'arg' must be a str or a float, not a {type(arg)}")

	@classmethod
	def convert_value(cls, value: float, to_: Union[str, float, Prefix], from_: Union[str, float, Prefix] = None) -> float:
		try:
			value = float(value)
		except Exception:
			raise ValueError(f"'value' must be a float, not a {type(value)}")

		if isinstance(to_, (str, float)):
			to_ = cls.get_prefix(to_)
		elif not isinstance(to_, Prefix):
			raise ValueError(f"'to_' must be a str, float or a Prefix, not a {type(to_)}")

		if isinstance(from_, (str, float)):
			from_ = cls.get_prefix(from_)
		elif from_ is None:
			from_ = cls.none
		elif not isinstance(from_, Prefix):
			raise ValueError(f"'from_' must be a str, float or a Prefix, not a {type(from_)}")

		return value / (to_.value / from_.value)


class Unit:
	_name: str = ""
	_symbol: str = ""
	_description: str = ""
	_base_unit: bool = False

	def __init__(self, name: str, symbol: str, description: str = ""):
		self.name = name
		self.symbol = symbol
		self.description = description

	def __repr__(self) -> str:
		return f"<Units {self.name} ({self.symbol}). {self.description}>"

	def __str__(self) -> str:
		return f"{self.name} ({self.symbol})"

	@property
	def name(self) -> str:
		return self._name

	@property
	def symbol(self) -> str:
		return self._symbol

	@property
	def description(self) -> str:
		return self._description

	@name.setter
	def name(self, new_name: str):
		if not isinstance(new_name, str):
			raise ValueError(f"'name' must be a str not a {type(new_name)}")
		self._name = new_name
			
	@symbol.setter
	def symbol(self, new_symbol: str):
		if not isinstance(new_symbol, str):
			raise ValueError(f"'symbol' must be a str not a {type(new_name)}")
		self._symbol = new_symbol

	@description.setter
	def description(self, new_desc: str):
		if not isinstance(new_desc, str):
			raise ValueError(f"'description' must be a str not a {type(new_desc)}")
		self._description = new_desc

	def is_base_unit(self) -> bool:
		return self._base_unit

	def is_derived_unit(self) -> bool:
		return not self._base_unit

	def name_with_prefix(self, prefix: Union[str, Prefix]) -> str:
		if isinstance(prefix, Prefix):
			return prefix.name + self.name
		elif isinstance(prefix, str):
			return getattr(PrefixEnum, prefix).name + self.name
		raise ValueError(f"'prefix' must be a str or a Prefix, not {type(prefix)}")

	def symbol_with_prefix(self, prefix: Union[str, float, Prefix]) -> str:
		if isinstance(prefix, Prefix):
			return prefix.symbol + self.name
		elif isinstance(prefix, (str, float)):
			return PrefixEnum.get_prefix(prefix).symbol + self.symbol
		raise ValueError(f"'prefix' must be a str or a Prefix, not {type(prefix)}")


class BaseUnit(Unit):
	_base_unit = True

	@staticmethod
	def metre():
		return BASE_UNITS['metre']

	@staticmethod
	def meter():
		return BASE_UNITS['meter']

	@staticmethod
	def second():
		return BASE_UNITS['second']

	@staticmethod
	def kelvin():
		return BASE_UNITS['kelvin']

	@staticmethod
	def mole():
		return BASE_UNITS['mole']

	@staticmethod
	def ampere():
		return BASE_UNITS['ampere']

	@staticmethod
	def candela():
		return BASE_UNITS['candela']

	@staticmethod
	def radian():
		return BASE_UNITS['radian']

	@staticmethod
	def steradian():
		return BASE_UNITS['steradian']


BASE_UNITS = {
	'metre': BaseUnit('Metre', 'm', description="The base unit of lenght."),
	'meter': BaseUnit('Meter', 'm', description="The base unit of lenght"),
	'second': BaseUnit('Second', 's', description="The base unit of time"),
	'kelvin': BaseUnit('Kelvin', 'K', description="The base unit of temperature"),
	'mole': BaseUnit('Mole', 'mol', description="The base unit of amount of substance"),
	'ampere': BaseUnit('Ampere', 'A', description="The base unit of electric current"),
	'candela': BaseUnit('Candela', 'cd', description="The base unit of luminous intensity"),
	'radian': BaseUnit('Radian', 'rad', description="The base unit of plane angle"),
	'steradian': BaseUnit('Steradian', 'sr', description="The base unit of solid angle")
}