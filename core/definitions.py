from .def_util import Call, Symbol, Number


definitions = [
    # {"given_name": String("john"), "surname": String("woods")},
    # {
    #     "name": Call("formatString", format="$given_name $surname"),
    # },
    {
        "y": Call(
            "add", left=Call("mul", left=Symbol("x"), right=Number(2)), right=Number(4)
        )
    },
]


# y = add(x, 4)
# x = sub(y, 4)

# name = "$given_name $surname"

# name = "john woods"

# given_name = pickString($name, "given_name")
