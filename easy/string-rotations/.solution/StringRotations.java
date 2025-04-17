public class StringRotations {
    enum Direction {
        LEFT,
        RIGHT
    }

    public static String rotate(String s, int k, Direction direction) {
        if (s.isEmpty() || s.length() == 1) {
            return s;
        }

        if (k < 0) {
            k = -k;
            direction = (direction == Direction.LEFT) ? Direction.RIGHT : Direction.LEFT;
        }

        int n = s.length();
        k = k % n;
        if (direction == Direction.LEFT) {
            return s.substring(k) + s.substring(0, k);
        } else { // Direction.RIGHT
            return s.substring(n - k) + s.substring(0, n - k);
        }
    }

    private static void test(String input, Direction direction, int k) {
        System.out.print("(\"" + input + "\", " + direction + ", " + k + "): ");
        System.out.println(rotate(input, k, direction));
    }

    public static void main(String[] args) {
        test("Texas", Direction.LEFT, 1);
        test("Florida", Direction.RIGHT, 1);
        test("Texas", Direction.LEFT, 3);
        test("Florida", Direction.RIGHT, 3);
        test("Texas", Direction.LEFT, 5);
        test("Florida", Direction.RIGHT, 5);
        test("Texas", Direction.LEFT, 0);
        test("Florida", Direction.RIGHT, 0);
        test("Texas", Direction.LEFT, 800);
        test("Florida", Direction.RIGHT, 800);
        test("Texas", Direction.LEFT, 77);
        test("Florida", Direction.RIGHT, 77);
        test("Texas", Direction.RIGHT, -2);
        test("Florida", Direction.LEFT, -2);
    }
}
