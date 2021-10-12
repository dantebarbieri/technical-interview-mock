# String Rotations
The concept of string rotations is a generalization of rotations of binary strings. Implement a function that takes the direction of a shift (left or right) as well as a number of places to shift (this can be negative, in which case, reverse the direction). This function should also take a string as a parameter and should shift the letters in the string the number of places desired and rotate the letters around for when they would shift off of the ends.

## Example
`"Texas", LEFT, 1` $\Rightarrow$ exasT

`"Texas", LEFT, 3` $\Rightarrow$ asTex

`"Texas", LEFT, 5` $\Rightarrow$ Texas

`"Texas", LEFT, 0` $\Rightarrow$ Texas

`"Texas", LEFT, 800` $\Rightarrow$ Texas

`("Texas", LEFT, 77), RIGHT, -2` $\Rightarrow$ sTexa