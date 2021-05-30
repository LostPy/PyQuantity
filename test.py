from pyquantity import PrefixEnum, BaseUnit, Quantity


def test_prefix():
	print([mb for mb in dir(PrefixEnum) if not mb.startswith('_')])
	print(PrefixEnum.hecto.name, PrefixEnum.hecto.symbol, PrefixEnum.hecto.value)
	
	PrefixEnum.add_prefix('custom', 'R', 1e30)
	print(PrefixEnum.custom)

	PrefixEnum.remove_prefix('custom')
	print([mb for mb in dir(PrefixEnum) if not mb.startswith('_')])


def base_unit():
	meter = BaseUnit.meter()
	print(meter)
	print('meter is a base unit: ', meter.is_base_unit())
	print('meter is a derived unit: ', meter.is_derived_unit())
	print('str(meter) = ', str(meter))


def test_quantity():
	q = Quantity(10.5, BaseUnit.meter())
	print(q)
	print('str(q): ', str(q))
	print('q.hecto(): ', q.hecto())
	print('q.n: ', q.n)
	print('q.G: ', q.G)
	q.k = 2
	print('q.value', q.value)


def test_operations():
	q1 = Quantity(10.3, BaseUnit.meter())
	q2 = Quantity(21.3, BaseUnit.meter())
	print(q1 < q2)
	print(q1 == q2)
	print(q1 > 15)
	print(q2 > 15)

	print(-q1)
	print(+q2)
	print(q1 * 4)
	print(q1 + q2)


if __name__ == '__main__':
	#test_prefix()
	#base_unit()
	#test_quantity()
	test_operations()
