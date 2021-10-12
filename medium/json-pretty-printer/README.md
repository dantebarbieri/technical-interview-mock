# JSON Pretty Printer
Write a function that takes in a string of valid JSON with no extra whitespace characters and "pretty print" the string by separating key-value pairs onto separate lines and indenting and separating brackets ('{', '[', ']', & '}') onto their own lines with a reasonable number of tabs/spaces for indentation.

## Example
Input
```json
{"name":"Dante","age":22,"weight":11.46,"friends":["Furkan","Mari","Alex","Carlos","Ajay"],"courses":[{"title":"Computer Graphics","department":"CSCE","number":441,"section":500},{"title":"Honors, Structrual Methods of Combinatorics","department":"MATH","number":431,"section":200}]}
```
As a string in whatever language you choose.

Output
```json
{
    "name":"Dante",
    "age":22,
    "weight":11.46,
    "friends":[
        "Furkan",
        "Mari",
        "Alex",
        "Carlos",
        "Ajay"
    ],
    "courses":[
        {
            "title":"Computer Graphics",
            "department":"CSCE",
            "number":441,
            "section":500
        },
        {
            "title":"Honors, Structrual Methods of Combinatorics",
            "department":"MATH",
            "number":431,
            "section":200
        }
    ]
}
```
This is one possible output. You may decide to handle the start of lists and objects differently and may also choose to insert a space (or other whitespace characters) before and/or after the colon key-value separators.