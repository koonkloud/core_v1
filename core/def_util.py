def Base(type: str, **kwargs):
    return {"type": type, **kwargs}


def String(value: str):
    return Base("string", value=value)


def Number(value: int):
    return Base("number", value=value)


def Call(functionName: str, **kwargs):
    return Base("call", fn=functionName, args=kwargs)


def Symbol(name: str):
    return Base("symbol", name=name)
