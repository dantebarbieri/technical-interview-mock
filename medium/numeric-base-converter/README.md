# Numeric Base Converter
Given a positive integer, $1<b<62$, representing a numeric base, write a function that takes in a number `n` and returns a string of `n` converted to base $b$. Use `[A-Z]` when you run out of digits and `[a-z]` if you run out of capital letters. As a bonus, if the problem is too easy, implement the ability to output in Roman numerals instead of a numeric base, if $b=476$ (the year of the Fall of the Western Roman Empire).

## Example
$b=2$, `n=10` $\Rightarrow$ `"1010"`

$b=8$, `n=10` $\Rightarrow$ `"12"`

$b=16$, `n=10` $\Rightarrow$ `"A"`

$b=11$, `n=10` $\Rightarrow$ `"A"`

$b=45$, `n=2186725` $\Rightarrow$ `"Nice"`

$b=10$, `n=8675309` $\Rightarrow$ `"8675309"`

## Roman Numerals
| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Individual Decimal Places
| | Thousands | Hundreds | Tens | Units |
|-|-----------|----------|------|-------|
|1| M         | C        | X    | I     |
|2| MM        | CC       | XX   | II    |
|3| MMM       | CCC      | XXX  | III   |
|4|           | CD       | XL   | IV    |
|5|           | D        | L    | V     |
|6|           | DC       | LX   | VI    |
|7|           | DCC      | LXX  | VII   |
|8|           | DCCC     | LXXX | VIII  |
|9|           | CM       | XC   | IX    |