"""Module with common quantities"""
from . import Quantity, BaseUnit, DerivedUnit, PrefixEnum, Prefix
from . import errors


class Time(Quantity):
	
	def __init__(self, value: float, prefix: Prefix = PrefixEnum.none):
		Quantity.__init__(self, value, unit=BaseUnit.second(), base_prefix=PrefixEnum.none, prefix=prefix)


class Lenght(Quantity):
	
	def __init__(self, value: float, prefix: Prefix = PrefixEnum.none):
		Quantity.__init__(self, value, unit=BaseUnit.metre(), base_prefix=PrefixEnum.none, prefix=prefix)


class Mass(Quantity):
	
	def __init__(self, value: float, prefix: Prefix = PrefixEnum.kilo):
		Quantity.__init__(self, value, unit=BaseUnit.gram(), base_prefix=PrefixEnum.kilo, prefix=prefix)


class Velocity(Quantity):
	
	def __init__(self, value: float, prefix: Prefix = PrefixEnum.none):
		raise NotImplemented


class AbsoluteTemperature(Quantity):

	ORIGIN_CELCIUS = -273.15
	ORIGIN_FAHRENHEIT = -459.67
	
	def __init__(self, value: float, prefix: Prefix = PrefixEnum.none):
		Quantity.__init__(self, value, unit=BaseUnit.kelvin(), base_prefix=PrefixEnum.none, prefix=prefix)

	@property
	def celcius(self) -> float:
		return self._value + self.ORIGIN_CELCIUS

	@property
	def fahrenheit(self) -> float:
		return self._value + self.ORIGIN_FAHRENHEIT

	@celcius.setter
	def celcius(self, new_value: float):
		self.value = new_value - self.ORIGIN_CELCIUS

	@fahrenheit.setter
	def fahrenheit(self, new_value: float):
		self.value = new_value - self.ORIGIN_FAHRENHEIT

	@classmethod
	def from_celcius(cls, value: float):
		return AbsoluteTemperature(value - self.ORIGIN_CELCIUS)

	@classmethod
	def from_fahrenheit(cls, value: float):
		return AbsoluteTemperature(value - self.ORIGIN_FAHRENHEIT)


class CelsiusTemperature(Quantity):
	
	def __init__(self, value: float):
		Quantity.__init__(self, value, unit=DerivedUnit.celcius(), base_prefix=PrefixEnum.none, prefix=PrefixEnum.none)

	def value_to_prefix(self, prefix: Prefix) -> float:
		raise errors.NoPrefixSupported()

	def set_value_from_prefix(self, new_value: float, prefix: Prefix):
		raise errors.NoPrefixSupported()

	@property
	def kelvin(self) -> float:
		return self._value - AbsoluteTemperature.ORIGIN_CELCIUS

	@property
	def fahrenheit(self) -> float:
		return 1.8 * self._value + 32.

	@kelvin.setter
	def kelvin(self, new_value: float):
		self.value = new_value + AbsoluteTemperature.ORIGIN_CELCIUS

	@fahrenheit.setter
	def fahrenheit(self, new_value: float):
		self.value = 5/9 (new_value - 32.)

	def get_absolute_instance(self) -> AbsoluteTemperature:
		return AbsoluteTemperature(self.kelvin)

	@classmethod
	def from_kelvin(cls, value: float):
		return cls(value + AbsoluteTemperature.ORIGIN_CELCIUS)

	@classmethod
	def from_fahrenheit(cls, value: float):
		return cls(5/9 (value - 32.))

	@classmethod
	def from_absolute_instance(cls, temperature: AbsoluteTemperature):
		if not isinstance(temperature, AbsoluteTemperature):
			raise ValueError(f"'temperature' must be an instance of AbsoluteTemperature, not {type(temperature)}")
		return cls(temperature.celcius)


