# Numbers to English
Write a program that takes in a number `n` and returns a string representing the way to say this number in English. It should work for integers in the range `[-100,000,000, 100,000,000]`. Another implementation if this is too easy or too difficult is to write a solution that can also handle floating points up to a given precision value.

## Example
The (and) and hyphen (-) characters are optional in the below outputs.

Commas are shown below to help chunk the number, but they are not present in the numeric type received unless it benefits your solution.

You can also choose to use the word "minus" instead of "negative" and "stop" or "dot instead of "point".

`12,345,678` $\Rightarrow$ twelve-million three-hundred (and) forty-five-thousand six-hundred (and) seventy-eight

`-19,990,121` $\Rightarrow$ negative nineteen-million nine-hundred (and) ninety-thousand one-hundred (and) twenty-one

`0` $\Rightarrow$ zero

`3.14159265, precision=4` $\Rightarrow$ three point one four one six

`1.25, precision=6` $\Rightarrow$ one point two five

`2.0000000000000001, precision=2` $\Rightarrow$ two

`10.500000001, precision=3` $\Rightarrow$ ten point five

`-4.444444, precision=5` $\Rightarrow$ negative four point four four four four four