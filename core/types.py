def Base(type: str, **kwargs):
    return {"type": type, **kwargs}


def String(value: str):
    return Base("string", value=value)


def Call(functionName: str, **kwargs):
    return Base("call", fn=functionName, args=kwargs)
