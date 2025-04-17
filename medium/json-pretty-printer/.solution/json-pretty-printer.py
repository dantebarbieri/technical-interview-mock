INDENTION = " " * 4

def pretty_print(compact_json: str) -> str:
    indentiation_level = 0
    pretty_json = ""
    in_string = False
    for i, char in enumerate(compact_json):
        if char == '"' and (i == 0 or compact_json[i - 1] != '\\'):
            in_string = not in_string
            pretty_json += char
        elif in_string:
            pretty_json += char
        else:
            if char == '{' or char == '[':
                pretty_json += char + "\n" + INDENTION * (indentiation_level + 1)
                indentiation_level += 1
            elif char == '}' or char == ']':
                indentiation_level -= 1
                pretty_json += "\n" + INDENTION * indentiation_level + char
            elif char == ',':
                pretty_json += char + "\n" + INDENTION * indentiation_level
            elif char == ':':
                pretty_json += char + " "
            else:
                pretty_json += char
    return pretty_json.strip()

if __name__ == "__main__":
    test_cases = [
        (
            '{"a":1,"b":2}',
            """{
    "a": 1,
    "b": 2
}""".strip()
        ),
        (
            '{"a":1,"b":{"c":3,"d":4}}',
            """{
    "a": 1,
    "b": {
        "c": 3,
        "d": 4
    }
}""".strip()
        ),
        (
            '[1,2,3]',
            """[
    1,
    2,
    3
]""".strip()
        ),
        (
            '[1,[2,3],4]',
            """[
    1,
    [
        2,
        3
    ],
    4
]""".strip()
        ),
        (
            '{"a":[1,2,3],"b":{"c":4}}',
            """{
    "a": [
        1,
        2,
        3
    ],
    "b": {
        "c": 4
    }
}""".strip()
        ),
        (
            '{"a":{"b":{"c":{"d":"e"}}}}',
            """{
    "a": {
        "b": {
            "c": {
                "d": "e"
            }
        }
    }
}""".strip()
        ),
        (
            '{"a":[{"b":"c"},{"d":"e"}]}',
            """{
    "a": [
        {
            "b": "c"
        },
        {
            "d": "e"
        }
    ]
}""".strip()
        ),
    ]

    for i, (input_str, expected) in enumerate(test_cases, start=1):
        result = pretty_print(input_str)
        assert result == expected, f"Test case {i} failed:\nExpected:\n{expected!r}\nGot:\n{result!r}"
    print("All test cases passed!")