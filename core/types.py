class Call:
    def __init__(self, fnName: str, args: object) -> None:
        self.fnName = fnName
        self.args = args


class Definition:
    def __init__(self, name: str, value: any) -> None:
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f"<{self.name} = {self.value}>"
