fn main() {
    println!("Run `cargo test` from the brace-matching-rust directory.");
}

#[allow(unused)]
fn fibonacci_slow(n: u128) -> u128 {
    match n {
        0 | 1 => 1,
        _ => fibonacci_slow(n - 1) + fibonacci_slow(n - 2),
    }
}

fn fibonacci_dp_helper(lut: &mut Vec<u128>, n: u128) -> u128 {
    if let Some(&answer) = lut.get(n as usize) {
        return answer;
    }
    let computed = fibonacci_dp_helper(lut, n - 1) + fibonacci_dp_helper(lut, n - 2);
    lut.push(computed);
    computed
}

#[allow(unused)]
fn fibonacci_dp(n: u128) -> u128 {
    let mut lut = vec![1, 1];
    fibonacci_dp_helper(&mut lut, n)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_fibonacci_slow_base_case() {
        assert_eq!(fibonacci_slow(0), 1);
        assert_eq!(fibonacci_slow(1), 1);
    }

    #[test]
    fn test_fibonacci_dp_base_case() {
        assert_eq!(fibonacci_dp(0), 1);
        assert_eq!(fibonacci_dp(1), 1);
    }

    #[test]
    fn test_fibonacci_slow_values() {
        assert_eq!(fibonacci_slow(5), 8);
        assert_eq!(fibonacci_slow(20), 10946);
        assert_eq!(fibonacci_slow(30), 1346269);
        assert_eq!(fibonacci_slow(40), 165580141);
        assert_eq!(fibonacci_slow(45), 1836311903);
    }

    #[test]
    fn test_fibonacci_dp_values() {
        assert_eq!(fibonacci_dp(5), 8);
        assert_eq!(fibonacci_dp(20), 10946);
        assert_eq!(fibonacci_dp(30), 1346269);
        assert_eq!(fibonacci_dp(40), 165580141);
        assert_eq!(fibonacci_dp(45), 1836311903);
    }
}
