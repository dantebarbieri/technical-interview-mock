# Recursively Print K-ary Tree
Write a function that recursively pretty-prints a k-ary tree in a nice hierarchy (can be rotated). The tree's members can be assumed to be printable and the tree's children can be assumed to be in an iterable structure.

## Examples
Centered (super hard)
```
            3
    1           10      12
0       8       6       5
        14
```

Left-Aligned (somewhat hard)
```
3
1       10  12
0   8   6   5
    14
```

Rotated (easy-ish)
```
    12
        5
        6
    10
3
        8
            14
    1
        0
```