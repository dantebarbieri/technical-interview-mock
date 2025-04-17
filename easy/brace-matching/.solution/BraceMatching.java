import java.util.Stack;

public class BraceMatching {
    private static boolean isMatchingPair(char opening, char closing) {
        return (opening == '(' && closing == ')') ||
               (opening == '{' && closing == '}') ||
               (opening == '[' && closing == ']');
    }

    public static boolean isBalanced(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } else if (c == ')' || c == '}' || c == ']') {
                if (stack.isEmpty())
                    return false;
                char top = stack.pop();
                if (!isMatchingPair(top, c))
                    return false;
            }
        }
        return stack.isEmpty();
    }
    
    private static void test(String input) {
        System.out.print("\"" + input + "\": ");
        if (isBalanced(input)) {
            System.out.println("Balanced");
        } else {
            System.out.println("Not Balanced");
        }
    }

    public static void main(String[] args) {
        test("");
        test("(");
        test("()");
        test("(]");
        test("{[}]");
        test("{[()]}");
        test("{[(])}");
        test("{[]()}");
    }
}