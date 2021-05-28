from typing import Union

from . import PrefixEnum, Unit, BASE_UNITS
from .unit import Prefix
from . import errors


class Quantity:
	_unit = None  # define the units of quantity
	_base_prefix = PrefixEnum.none  # define the base prefix of quantity. For example, for the mass it's 'kilo'.

	def __init__(self, value: float, unit: Union[str, Unit], base_prefix: Union[str, float, Prefix] = PrefixEnum.none, prefix: Prefix = None):
		"""Initialize an instance of Quantity
	
		Parameters
		----------
		None
		"""
		self.base_prefix = base_prefix
		if (prefix is None and self._base_prefix.value == 1) or (isinstance(prefix, Prefix) and prefix.value == 1):
			# value with a prefix of value = 1
			self._value = value

		elif prefix is None or (isinstance(prefix, Prefix) and prefix.value == slef.base_prefix.value):
			# value with the base prefix
			self._value = PrefixEnum.convert_value(value, to_=PrefixEnum.none, from_=self._base_prefix)

		elif isinstance(prefix, Prefix):
			# value with other prefix
			self._value = PrefixEnum.convert_value(value, to_=PrefixEnum.none, from_=prefix)

		else:
			raise ValueError(f"'prefix' argument must be a Prefix, not {type(prefix)}")

		self.unit = unit

	def __repr__(self) -> str:
		"""repr(self)"""
		return f"<{self.name}: {self._value} {self.unit.symbol_with_prefix(self._base_prefix)}>"

	def __str__(self) -> str:
		"""str(self)"""
		return f"{self._value} {self.unit.symbol_with_prefix(self._base_prefix)}"

	def __format__(self, fmt_spec: str = "") -> str:
		"""format(self, str)"""
		return format(str(self), format_spec=fmt_spec)

	def __add__(self, other):
		"""self + other"""
		raise NotImplemented

	def __sub__(self, other):
		"""self - other"""
		raise NotImplemented

	def __mul__(self, other):
		"""self * other"""
		raise NotImplemented

	def __floordiv__(self, other):
		"""self // other"""
		raise NotImplemented

	def __div__(self, other):
		"""self / other"""
		raise NotImplemented

	def __pow__(self, other):
		"""self ** other"""
		raise NotImplemented

	def __iadd__(self, other):
		"""self += other"""
		raise NotImplemented

	def __isub__(self, other):
		"""self -= other"""
		raise NotImplemented

	def __imul__(self, other):
		"""self *= other"""
		raise NotImplemented

	def __ifloordiv__(self, other):
		"""self //= other"""
		raise NotImplemented

	def __idiv__(self, other):
		"""self /= other"""
		raise NotImplemented

	def __ipow__(self, other):
		"""self **= other"""
		raise NotImplemented

	def __pos__(self):
		""" + self"""
		raise NotImplemented

	def __neg__(self):
		"""- self"""
		raise NotImplemented

	def __abs__(self):
		""" abs(self)"""
		raise NotImplemented

	def __int__(self) -> int:
		"""int(self)"""
		return int(self._value)

	def __float__(self) -> float:
		"""float(self)"""
		return float(self._value)

	def __lt__(self, other) -> bool:
		"""self < other"""
		raise NotImplemented

	def __le__(self, other) -> bool:
		"""self <= other"""
		raise NotImplemented

	def __eq__(self, other) -> bool:
		"""self == other"""
		raise NotImplemented

	def __ne__(self, other) -> bool:
		"""self != other"""
		raise NotImplemented

	def __gt__(self, other) -> bool:
		"""self > other"""
		raise NotImplemented

	def __ge__(self, other) -> bool:
		"""self >= other"""
		raise NotImplemented

	def _format_real_value(self) -> str:
		if abs(self._value) >= 1000:
			return f"{self._value:.3e}"
		return f"{self._value:.3f}"

	def value_to_prefix(self, prefix: Prefix) -> float:
		if not isinstance(prefix, Prefix):
			raise ValueError(f"'prefix' must be a Prefix, not a {type(prefix)}")
		return PrefixEnum.convert_value(self.value, to_=prefix)

	def set_value_from_prefix(self, new_value: float, prefix: Prefix):
		try:
			new_value = float(new_value)
		except Exception:
			raise ValueError(f"'new_value' must be a float, not a {type(new_value)}")

		if not isinstance(prefix, Prefix):
			raise ValueError(f"'prefix' must be a Prefix, not a {type(prefix)}")

		self._value = PrefixEnum.convert_value(new_value, to_=PrefixEnum.none, from_=prefix)

	def yotta(self) -> float:
		return self.value_to_prefix(PrefixEnum.yotta)

	def zetta(self) -> float:
		return self.value_to_prefix(PrefixEnum.zetta)

	def exa(self) -> float:
		return self.value_to_prefix(PrefixEnum.exa)

	def peta(self) -> float:
		return self.value_to_prefix(PrefixEnum.peta)

	def tera(self) -> float:
		return self.value_to_prefix(PrefixEnum.tera)

	def giga(self) -> float:
		return self.value_to_prefix(PrefixEnum.giga)

	def mega(self) -> float:
		return self.value_to_prefix(PrefixEnum.mega)

	def kilo(self) -> float:
		return self.value_to_prefix(PrefixEnum.kilo)

	def hecto(self) -> float:
		return self.value_to_prefix(PrefixEnum.hecto)

	def deca(self) -> float:
		return self.value_to_prefix(PrefixEnum.deca)

	def no_prefix(self) -> float:
		return self.value

	def deci(self) -> float:
		return self.value_to_prefix(PrefixEnum.deci)

	def centi(self) -> float:
		return self.value_to_prefix(PrefixEnum.centi)

	def mili(self) -> float:
		return self.value_to_prefix(PrefixEnum.mili)

	def micro(self) -> float:
		return self.value_to_prefix(PrefixEnum.micro)

	def nano(self) -> float:
		return self.value_to_prefix(PrefixEnum.nano)

	def pico(self) -> float:
		return self.value_to_prefix(PrefixEnum.pico)

	def femto(self) -> float:
		return self.value_to_prefix(PrefixEnum.femto)

	def atto(self) -> float:
		return self.value_to_prefix(PrefixEnum.atto)

	def zepto(self) -> float:
		return self.value_to_prefix(PrefixEnum.zepto)

	def yocto(self) -> float:
		return self.value_to_prefix(PrefixEnum.yocto)

	def set_yotta(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.yotta)

	def set_zetta(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.zetta)

	def set_exa(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.exa)

	def set_peta(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.peta)

	def set_tera(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.tera)

	def set_giga(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.giga)

	def set_mega(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.mega)

	def set_kilo(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.kilo)

	def set_hecto(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.hecto)

	def set_deca(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.deca)

	def set_no_prefix(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.none)

	def set_deci(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.deci)

	def set_centi(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.centi)

	def set_mili(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.mili)

	def set_micro(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.micro)

	def set_nano(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.nano)

	def set_pico(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.pico)

	def set_femto(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.femto)

	def set_atto(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.atto)

	def set_zepto(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.zepto)

	def set_yocto(self, new_value: float):
		self.set_value_from_prefix(new_value, PrefixEnum.yocto)

	@classmethod
	def get_name(cls) -> str:
		return cls.__name__

	@property
	def unit(self) -> Unit:
		return self._unit

	@unit.setter
	def unit(self, new_unit: Union[str, Unit]):
		if isinstance(new_unit, str):
			self._unit = Unit(new_unit, new_unit)
		elif isinstance(new_unit, Unit):
			self._unit = new_unit
		else:
			raise ValueError(f"'unit' must be a string which define the symbol of unit or an instance of Unit, not {type(new_unit)}")

	@property
	def base_prefix(self) -> Prefix:
		return self._base_prefix

	@base_prefix.setter
	def base_prefix(self, prefix: Union[str, float, Prefix]):
		if isinstance(prefix, Prefix):
			self._base_prefix = prefix
		elif isinstance(prefix, str) or isinstance(prefix, float):
			PrefixEnum.get_prefix(prefix)
		else:
			raise ValueError(f"'prefix' must be a str, a float or a Prefix, not a {type(prefix)}")

	@property
	def value(self) -> float:
		return self._value

	@value.setter
	def value(self, new_value: float):
		if isinstance(new_value, float) and self._base_prefix.value == 1:
			self._value = new_value
		elif isinstance(new_value, float):
			self.set_value_from_prefix(new_value, to_=PrefixEnum.none, from_=self._base_prefix)
		raise ValueError(f"'value' must be a float, not {type(new_value)}")

	@property
	def name(self) -> str:
		return self.get_name()

	@property
	def Y(self) -> float:
		return self.yotta()

	@property
	def Z(self) -> float:
		return self.zetta()

	@property
	def E(self) -> float:
		return self.exa()

	@property
	def P(self) -> float:
		return self.peta()

	@property
	def T(self) -> float:
		return self.tera()

	@property
	def G(self) -> float:
		return self.giga()

	@property
	def M(self) -> float:
		return self.mega()

	@property
	def k(self) -> float:
		return self.kilo()

	@property
	def h(self) -> float:
		return self.hecto()

	@property
	def da(self) -> float:
		return self.deca()

	@property
	def none(self) -> float:
		return self._value

	@property
	def d(self) -> float:
		return self.deci()

	@property
	def c(self) -> float:
		return self.centi()

	@property
	def m(self) -> float:
		return self.mili()

	@property
	def u(self) -> float:
		return self.micro()

	@property
	def n(self) -> float:
		return self.nano()

	@property
	def p(self) -> float:
		return self.pico()

	@property
	def f(self) -> float:
		return self.femto()

	@property
	def a(self) -> float:
		return self.atto()

	@property
	def z(self) -> float:
		return self.zepto()

	@property
	def y(self) -> float:
		return self.yocto()

	@Y.setter
	def Y(self, new_value: float):
		return self.set_yotta(new_value)

	@Z.setter
	def Z(self, new_value: float):
		return self.set_zetta(new_value)

	@E.setter
	def E(self, new_value: float):
		return self.set_exa(new_value)

	@P.setter
	def P(self, new_value: float):
		return self.set_peta(new_value)

	@T.setter
	def T(self, new_value: float):
		return self.set_tera(new_value)

	@G.setter
	def G(self, new_value: float):
		return self.set_giga(new_value)

	@M.setter
	def M(self, new_value: float):
		return self.set_mega(new_value)

	@k.setter
	def k(self, new_value: float):
		return self.set_kilo(new_value)

	@h.setter
	def h(self, new_value: float):
		return self.set_hecto(new_value)

	@da.setter
	def da(self, new_value: float):
		return self.set_deca(new_value)

	@none.setter
	def none(self, new_value: float):
		return self.set_no_prefix(new_value)

	@d.setter
	def d(self, new_value: float):
		return self.set_deci(new_value)

	@c.setter
	def c(self, new_value: float):
		return self.set_centi(new_value)

	@m.setter
	def m(self, new_value: float):
		return self.set_mili(new_value)

	@u.setter
	def u(self, new_value: float):
		return self.set_micro(new_value)

	@n.setter
	def n(self, new_value: float):
		return self.set_nano(new_value)

	@p.setter
	def p(self, new_value: float):
		return self.set_pico(new_value)

	@f.setter
	def f(self, new_value: float):
		return self.set_femto(new_value)

	@a.setter
	def a(self, new_value: float):
		return self.set_atto(new_value)

	@z.setter
	def z(self, new_value: float):
		return self.set_zepto(new_value)

	@y.setter
	def y(self, new_value: float):
		return self.set_yocto(new_value)
