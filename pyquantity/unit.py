from . import errors


class Prefix:
	__names_list: tuple = (
		'yotta',
		'zetta',
		'exa',
		'peta',
		'tera',
		'giga',
		'mega',
		'kilo',
		'hecto',
		'deca',
		'none',
		'deci',
		'centi',
		'mili',
		'micro',
		'nano',
		'pico',
		'femto',
		'atto',
		'zetta',
		'yocto'
	)

	__symbols_list: tuple = (
		'Y',
		'Z',
		'E',
		'P',
		'T',
		'G',
		'M',
		'k',
		'h',
		'da',
		'',
		'd',
		'c',
		'm',
		'u',
		'n',
		'p',
		'f',
		'a',
		'z',
		'y'
	)

	__values_list: tuple = (
		1e24,
		1e21,
		1e18,
		1e15,
		1e12,
		1e9,
		1e6,
		1e3,
		100,
		10,
		1,
		0.1,
		0.01,
		1e-3,
		1e-6,
		1e-9,
		1e-12,
		1e-15,
		1e-18,
		1e-21,
		1e-24,
	)
	symbols = dict(zip(__names_list, __symbols_list))
	values = dict(zip(__names_list, __values_list))

	@staticmethod
	def name_from_value(value: int) -> str:
		return dict(zip(__values_list, __names_list))[value]

	@staticmethod
	def symbol_from_value(value: int) -> str:
		return dict(zip(__values_list, __symbols_list))[value]

	@staticmethod
	def name_from_symbol(symbol: str) -> str:
		return dict(zip(__symbols_list, __names_list))[symbol]


class Unit:
	_name: str = ""
	_symbol: str = ""
	_description: str = ""
	_base_unit: bool = False

	def __init__(self, name: str, symbol: str, description: str = ""):
		self.name = name
		self.symbol = symbol
		self.description = description

	def __repr__(self):
		return f"Units {self.name} ({self.symbol}). {self.description}"

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
			raise ValueError(f"'name' must be a string not a {type(new_name)}")
		self._name = new_name
			
	@symbol.setter
	def symbol(self, new_symbol: str):
		if not isinstance(new_symbol, str):
			raise ValueError(f"'symbol' must be a string not a {type(new_name)}")
		self._symbol = new_symbol

	@description.setter
	def description(self, new_desc: str):
		if not isinstance(new_desc, str):
			raise ValueError(f"'description' must be a string not a {type(new_desc)}")
		self._description = description

	def is_base_unit(self) -> bool:
		return self._base_unit

	def is_derived_unit(self) -> bool:
		return not self._base_unit

	def get_with_prefix(self, prefix: str) -> str:
		return Prefix.symbols[prefix] + self.name


class BaseUnit(Unit):
	_base_unit = True

	@name.setter
	def name(self, new_name: str):
		raise errors.QuantityError("You cannot set the name of a base unit")

	@symbol.setter
	def symbol(self, new_symbol: str):
		raise errors.QuantityError("You cannot set the name of a base unit")

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