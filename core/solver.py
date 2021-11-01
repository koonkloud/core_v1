from .funcs import funcs
from .data import data


def solve(target):
	if target not in data:
		raise Exception("target not found")
	value = data[target]
	if type(value) is not dict:
		return value
	
	funcName = list(value.keys())[0]

	if funcName not in funcs:
		raise Exception("function '" + funcName + "' not found")


	func = funcs[funcName]
	funcArgs = value[funcName]

	args = []
	for _, arg in funcArgs.items():
		val = arg
		if type(arg) == str and arg[0] == '$':
			val = solve(arg[1:])
		args.append(val)

	return func['logic'](*args)
	
