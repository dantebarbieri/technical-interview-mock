def minimize(string: str) -> str:
    if not string:
        return string
    
    for i in range(1, len(string)):
        if string[i - 1] > string[i]:
            return string[:i - 1] + string[i:]
    return string[:-1]

if __name__ == "__main__":
    test_cases = [
        ("apple", "aple"),
        ("beatrice", "batrice"),
        ("tree", "ree"),
        ("", ""),
        ("a", ""),
        ("ab", "a"),
        ("ba", "a"),
        ("abc", "ab"),
        ("cba", "ba"),
        ("ABBA", "ABA"),
        ("ABBC", "ABB"),
        ("BAAB", "AAB"),
    ]

    for i, (input_str, expected) in enumerate(test_cases):
        result = minimize(input_str)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
    print("All test cases passed!")