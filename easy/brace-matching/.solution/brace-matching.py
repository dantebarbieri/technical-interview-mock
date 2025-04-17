OPEN_BRACKETS = {'(': ')', '{': '}', '[': ']', '<': '>'}
CLOSE_BRACKETS = OPEN_BRACKETS.values()

def brace_matching(string: str) -> bool:
    bracket_stack = []
    for char in string:
        if char in OPEN_BRACKETS:
            bracket_stack.append(char)
        elif char in CLOSE_BRACKETS:
            if not bracket_stack or OPEN_BRACKETS[bracket_stack.pop()] != char:
                return False
    return not bracket_stack

if __name__ == "__main__":
    test_cases = [
        ("", True),
        ("(", False),
        ("()", True),
        ("(]", False),
        (r"{[(<>)]}", True),
        ("{[(<>])}", False),
        (r"{[]<>()}", True),
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        result = brace_matching(input_str)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
    print("All test cases passed!")