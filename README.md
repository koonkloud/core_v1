# core_v1

The core of the KoonKloud

This is a very bare bones math solver.

We have a set of definitions:

```json
[
    {
        "y": 4
    },
    { "y": { "add": { "left": "$x", "right": -1 } } }
]
```

This is the same as writing

```
y = 4
y = x - 1
```

We can then use the `solve` function to solve for a variable.

```python
solve("y") # 4

solve("x") # 5
```
