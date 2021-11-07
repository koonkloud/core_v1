from core.definitions import definitions
from core.funcs import funcs
from core import Solver
from pprint import pprint

solver = Solver(definitions, funcs)
defs = solver.getDefinitions("x")
pprint(defs)
