# Brace Matching
Given a string, ensure that all opening braces have a matching closing brace and that braces are not mixed together, such as:
```
{[}]
```
This is an invalid input even though the numbers of each type of opening and closing brace match because a curly brace has been transposed with a square bracket. The program should return `true` for valid inputs and `false` otherwise. Inputs with no braces are always valid.

Challenge: Take in a set of pairs of opening and closing braces and use this set for lookups without hard-coding your own brace definitions.