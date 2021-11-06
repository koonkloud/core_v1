# core_v1

The core of the KoonKloud

## Definitions

Definitions are stored as a list of Definition types.

A definition type looks like:

```json
{
    "foo": {
        "type": "string",
        "value": "bar"
    }
}
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
