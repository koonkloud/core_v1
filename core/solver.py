from typing import List
from .types import Definition

from .util import equalsSymbol, isCall, parseDefinition
from .def_util import Call, Symbol


class Solver:
    definitions: List[Definition] = []
    baseFunctions: List[object] = []

    def __init__(
        self, definitions: List[object] = [], baseFunctions: List[object] = []
    ) -> None:
        self.loadDefinitions(definitions)
        self.loadBaseFunctions(baseFunctions)

    def loadDefinitions(self, definitions: List[object]) -> None:
        self.definitions = [parseDefinition(definition) for definition in definitions]

    def loadBaseFunctions(self, functions: List[object]) -> None:
        self.baseFunctions = functions

    def getDefinitions(self, name: str) -> List[Definition]:
        return self.getDirectDefinitions(name) + self.getIndirectDefinitions(name)

    def getDirectDefinitions(self, name: str) -> List[Definition]:
        return [
            definition for definition in self.definitions if definition.name == name
        ]

    def getIndirectDefinitions(self, name: str) -> List[Definition]:
        indirectDefinitions = []
        for definition in self.definitions:
            isolatedDefinition = self.getIndirectDefinition(definition, name)
            if isolatedDefinition:
                indirectDefinitions.append(isolatedDefinition)
        return indirectDefinitions

    def getIndirectDefinition(self, definition: Definition, name: str):
        defined = definition.name
        value = definition.value

        left = Symbol(defined)
        right = value

        return self.isolateSymbol(left, right, name)

    def isolateSymbol(self, left: object, right: object, target: str) -> object:
        funcName = right["fn"]
        funcArgs = right["args"]
        func = self.getFunction(funcName)
        for argName, arg in funcArgs.items():
            if self.containsSymbol(expr=arg, symbol=target):
                left = Call(func["reverse"], left=left, right=funcArgs["right"])
                right = arg
        if equalsSymbol(right, target):
            return left
        return self.isolateSymbol(left, right, target)

    def containsSymbol(self, expr: object, symbol: str) -> bool:
        return equalsSymbol(expr, symbol) or (
            isCall(expr)
            and any([self.containsSymbol(arg, symbol) for arg in expr["args"].values()])
        )

    def getFunction(self, functionName: str) -> object:
        functions = self.getFunctions()
        if functionName not in functions:
            raise Exception("func not found w name " + functionName)
        return functions[functionName]

    def getFunctions(self) -> List[object]:
        return self.baseFunctions
