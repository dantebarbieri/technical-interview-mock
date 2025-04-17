# String Rotations
The concept of string rotations is a generalization of rotations of binary strings. Implement a function that takes the direction of a shift (left or right) as well as a number of places to shift (this can be negative, in which case, reverse the direction). This function should also take a string as a parameter and should shift the letters in the string the number of places desired and rotate the letters around for when they would shift off of the ends.

## Example
`"Texas", LEFT, 1` $\Rightarrow$ exasT

`"Florida", RIGHT, 1` $\Rightarrow$ aFlorid

`"Texas", LEFT, 3` $\Rightarrow$ asTex

`"Florida", RIGHT, 3` $\Rightarrow$ idaFlor

`"Texas", LEFT, 5` $\Rightarrow$ Texas

`"Texas", LEFT, 0` $\Rightarrow$ Texas

`"Florida", RIGHT, 0` $\Rightarrow$ Florida

`"Texas", LEFT, 800` $\Rightarrow$ Texas

`("Texas", LEFT, 77), RIGHT, -2` $\Rightarrow$ sTexa