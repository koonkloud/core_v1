def fmtStr(*args):
    args = list(args)
    del args[0]
    return " ".join(args)


def pickStr(target, str, format: str):
    format = format.replace("\\", "")
    parts = str.split()
    formatParts = format.split()
    if len(parts) != len(formatParts):
        print("parts do not match")
        return
    partsDict = {}
    for i, part in enumerate(formatParts):
        partsDict[part[1:]] = parts[i]
    return partsDict[target]


funcs = {
    "add": {"logic": lambda l, r: l + r, "reverse": "sub"},
    "sub": {"logic": lambda l, r: l - r, "reverse": "add"},
    "mul": {"logic": lambda l, r: l * r, "reverse": "div"},
    "div": {"logic": lambda l, r: l / r, "reverse": "mul"},
    "formatString": {"logic": fmtStr, "reverse": "pickString"},
    "pickString": {"logic": pickStr, "reverse": "formatString"},
}
