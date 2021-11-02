data = [
    {
        "y": 4,
    },
    {"y": {"add": {"left": {"mul": {"left": "$x", "right": 2}}, "right": 1}}},
]

# y = 4
# y = Add(Mul(x, 2), 1)

# Min(y, 1) = Mul(x, 2)
# Div(Min(y, 1), 2) = x
# x = (y - 1) / 2
