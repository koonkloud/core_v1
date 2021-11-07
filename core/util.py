from .types import Definition


def parseDefinition(definition: object) -> Definition:
    definitionName = list(definition.keys())[0]
    definitionValue = definition[definitionName]
    return Definition(definitionName, definitionValue)


def equalsBlock(block: object, type: str) -> bool:
    return block["type"] == type


def isCall(block: object) -> bool:
    return equalsBlock(block, "call")


def equalsSymbol(block: object, name: str) -> bool:
    return equalsBlock(block, "symbol") and block["name"] == name
