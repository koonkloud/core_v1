from core.types import String, Call
from pprint import pprint


definitions = [
    {"given_name": String("john"), "surname": String("woods")},
    {
        "name": Call("fmt", fmt="$given_name $surname"),
    },
]

pprint(definitions)

# name = "$given_name $surname"

# name = "john woods"

# given_name = pickString($name, "given_name")
