fn main() {
    println!("Run `cargo test` from the brace-matching-rust directory.");
}

fn get_close_brace(open_brace: char) -> Option<char> {
    match open_brace {
        '[' => Some(']'),
        '{' => Some('}'),
        '(' => Some(')'),
        _ => None
    }
}

fn is_close_brace(c: char) -> bool {
    c == ']' || c == '}' || c == ')'
}

#[allow(unused)]
fn brace_match(s: &str) -> bool {
    let mut stack = vec![];
    for c in s.chars() {
        if is_close_brace(c) {
            match stack.last() {
                Some(back) => if &c == back {
                    stack.pop();
                },
                None => return false
            }
        }
        if let Some(close_brace) = get_close_brace(c) {
            stack.push(close_brace)
        }
    }
    stack.is_empty()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_brace_match_empty() {
        assert_eq!(brace_match(""), true);
    }

    #[test]
    fn test_brace_match_single() {
        assert_eq!(brace_match("{"), false);
        assert_eq!(brace_match("["), false);
        assert_eq!(brace_match("("), false);
        assert_eq!(brace_match("}"), false);
        assert_eq!(brace_match("]"), false);
        assert_eq!(brace_match(")"), false);
    }

    #[test]
    fn test_brace_match_pair() {
        assert_eq!(brace_match("{}"), true);
        assert_eq!(brace_match("[]"), true);
        assert_eq!(brace_match("()"), true);
    }

    #[test]
    fn test_brace_match_transpose() {
        assert_eq!(brace_match("{[}]"), false);
        assert_eq!(brace_match("{[(})]"), false);
    }

    #[test]
    fn test_brace_match_nested() {
        assert_eq!(brace_match("{[]}"), true);
        assert_eq!(brace_match("{()}"), true);
        assert_eq!(brace_match("[()]"), true);
        assert_eq!(brace_match("[{}]"), true);
        assert_eq!(brace_match("({})"), true);
        assert_eq!(brace_match("([])"), true);
    }

    #[test]
    fn test_brace_match_asymmetric() {
        assert_eq!(brace_match("{}[]"), true);
        assert_eq!(brace_match("()[]"), true);
        assert_eq!(brace_match("(){}"), true);
    }

    #[test]
    fn test_brace_match_non_braces() {
        assert_eq!(brace_match("{list: [e1, e2, e3]}"), true);
    }
}
