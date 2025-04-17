from enum import Enum

class Direction(Enum):
    LEFT = 1
    RIGHT = 2

def string_rotations(string: str, direction: Direction, num_shift: int) -> str:
    if not string:
        return string
    
    if num_shift < 0:
        num_shift = abs(num_shift)
        direction = Direction.RIGHT if direction == Direction.LEFT else Direction.LEFT

    num_shift %= len(string)
    if direction == Direction.LEFT:
        return string[num_shift:] + string[:num_shift]
    elif direction == Direction.RIGHT:
        return string[-num_shift:] + string[:-num_shift]
    else:
        raise ValueError("Invalid direction")

if __name__ == "__main__":
    test_cases = [
        ("Texas", Direction.LEFT, 1, "exasT"),
        ("Florida", Direction.RIGHT, 1, "aFlorid"),
        ("Texas", Direction.LEFT, 3, "asTex"),
        ("Florida", Direction.RIGHT, 3, "idaFlor"),
        ("Texas", Direction.LEFT, 5, "Texas"),
        ("Florida", Direction.RIGHT, 5, "oridaFl"),
        ("Texas", Direction.LEFT, 0, "Texas"),
        ("Florida", Direction.RIGHT, 0, "Florida"),
        ("Texas", Direction.LEFT, 800, "Texas"),
        ("Florida", Direction.RIGHT, 800, "daFlori"),
        ("Texas", Direction.LEFT, 77, "xasTe"),
        ("Florida", Direction.RIGHT, 77, "Florida"),
        ("Texas", Direction.RIGHT, -2, "xasTe"),
        ("Florida", Direction.LEFT, -2, "daFlori"),
    ]

    for i, (input_str, direction, num_shift, expected) in enumerate(test_cases):
        result = string_rotations(input_str, direction, num_shift)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
    print("All test cases passed!")