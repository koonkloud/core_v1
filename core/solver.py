from .funcs import funcs
from .data import data


def isolate(definition, target):
    definedName = list(definition.keys())[0]
    definedFunc: dict = definition[definedName]
    funcName = list(definedFunc.keys())[0]
    funcArgs = definedFunc[funcName]
    func = funcs[funcName]

    # check if the target is in 1 of the paramiters
    # NOTE: this will only check the LEFT arg
    if "$" + target == funcArgs["left"]:
        reverse = func["reverse"]
        return {reverse: {"left": "$" + definedName, "right": funcArgs["right"]}}


# determine if the target can be solved for
def getDefinitions(target):
    defs = []
    for definition in data:
        # direct def
        if target in definition:
            defs.append(definition[target])
        if type(list(definition.values())[0]) is dict:
            isolated = isolate(definition, target)
            if isolated:
                defs.append(isolated)
    return defs


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
    funcName = list(targetDef.keys())[0]

    if funcName not in funcs:
        raise Exception("function '" + funcName + "' not found")

    func = funcs[funcName]
    funcArgs = targetDef[funcName]

    args = []
    for _, arg in funcArgs.items():
        val = arg
        if type(arg) == str and arg[0] == "$":
            val = solve(arg[1:])
        args.append(val)

    return func["logic"](*args)
