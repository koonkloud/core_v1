from .defs import defs
from .data import data


def solve(target):
	if target in data:
		return data[target]
	if target not in defs:
		raise Exception("target not found")
	targetDef = defs[target]
	funcName = list(targetDef.keys())[0]
	func = targetDef[funcName]
	if funcName == 'add':
		l = func['left']
		r = func['right']
		if type(l) == str and l[0] == '$':
			l = solve(l[1:])
		if type(r) == str and r[0] == '$':
			r = solve(r[1:])
		return l + r
	else:
		raise Exception("unknown func")
	
