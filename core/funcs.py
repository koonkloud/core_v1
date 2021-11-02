funcs = {
    "add": {"logic": lambda l, r: l + r, "reverse": "sub"},
    "sub": {"logic": lambda l, r: l - r, "reverse": "add"},
    "mul": {"logic": lambda l, r: l * r, "reverse": "div"},
    "div": {"logic": lambda l, r: l / r, "reverse": "mul"},
    "concat": {
        "logic": lambda l, r: l + " " + r,
    },
}
