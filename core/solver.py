from .funcs import funcs
from .data import data


def parseEq(eq):
    op = list(eq.keys())[0]
    return op, eq[op]


def containsTarget(eq, target):
    if type(eq) is not dict:
        if eq == "$" + target:
            return True
        return
    op, eq = parseEq(eq)
    for argName, arg in eq.items():
        if containsTarget(arg, target):
            return True
    return


def isolateVar(left, right, target):

    funcName, args = parseEq(right)
    func = funcs[funcName]
    for argName, arg in args.items():
        if containsTarget(arg, target):
            left = {func["reverse"]: {"left": left, "right": args["right"]}}
            right = arg

    if "$" + target == right:
        return left

    return isolateVar(left, right, target)


def isolate(definition, target):
    definedName, definedFunc = parseEq(definition)
    funcName, funcArgs = parseEq(definedFunc)
    func = funcs[funcName]

    left = "$" + definedName
    right = definedFunc
    t = target

    return isolateVar(left, right, t)


# determine if the target can be solved for
def getDefinitions(target):
    defs = []
    for definition in data:
        # direct def
        if target in definition:
            defs.append(definition[target])
        elif type(list(definition.values())[0]) is dict:
            isolated = isolate(definition, target)
            if isolated:
                defs.append(isolated)
    return defs


def solveVar(eq):
    op, args = parseEq(eq)
    parsedArgs = []
    for _, arg in args.items():
        val = arg
        if type(arg) is dict:
            val = solveVar(arg)
        if type(arg) == str and arg[0] == "$":
            val = solve(arg[1:])
        parsedArgs.append(val)

    func = funcs[op]
    return func["logic"](*parsedArgs)


def solve(target):
    defs = getDefinitions(target)
    if not defs:
        raise Exception("target not found")

    if len(defs) > 1:
        for d in defs:
            if type(d) is not dict:
                return d
        print(defs)
        print("multiple definition formulas")
        return

    targetDef = defs[0]
    return solveVar(targetDef)
