data = [
    {"given_name": "john"},
    {"surname": "woods"},
    {
        "name": {
            "formatString": {"format": "\\$given_name $surname"},
            "params": ["given_name", "surname"],
        }
    },
]

# name = "$given_name $surname"

# name = "john woods"

# given_name = pickString($name, "given_name")
