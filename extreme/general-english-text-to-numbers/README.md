# General English Text to Numbers
Write a function that takes as input a string of English text and extracts numerals (e.g. "4", "700", etc.) as well as written numbers (e.g. "four", "seventy", "one-hundred") accounting for punctuation. The function should also handle "negative" and "minus" as keywords and should return an integer equivalent to what the user input. It should ignore all other text and symbols.

## Examples
`"one-hundred 72"` $\Rightarrow$ `172`

`"minus 800"` $\Rightarrow$ `-800`

`"negative ten thousand and 420"` $\Rightarrow$ `-10420`

`"five-hundred and sixty 9 dollars$"` $\Rightarrow$ `569`