long naive_fibonacci(int n) {
    if(n < 2) return 1;
    return naive_fibonacci(n-1) + naive_fibonacci(n-2);
}

#include <vector>
long fibonacci_helper(std::vector<long>& fibonacci_record, int n) {
    if(static_cast<unsigned>(n) < fibonacci_record.size()) { return fibonacci_record[n]; }
    fibonacci_record.push_back(fibonacci_helper(fibonacci_record, n-1) + fibonacci_helper(fibonacci_record, n-2));
    return fibonacci_record.back();
}

long fibonacci(int n) {
    std::vector<long> fibonacci_record = {1, 1};
    return fibonacci_helper(fibonacci_record, n);
}

#include <cmath>
long closed_form_fibonacci(int n) {
    constexpr long double GOLDEN_RATIO = 1.6180339887498948482045868343656381177203091798057628621354486227L;
    return static_cast<long>(
        std::roundl(
            (
                std::pow(GOLDEN_RATIO, (n+1))
                -std::pow(1-GOLDEN_RATIO, (n+1))
            )
            /std::sqrt(5)));
}

#include <iostream>
int main() {
    constexpr int BIG_NUMBER = 45;
    std::cout << "Fibonacci of " << BIG_NUMBER << std::endl;
    std::cout << "Closed Form: " << closed_form_fibonacci(BIG_NUMBER) << std::endl;
    std::cout << "Dynamic Programming: " << fibonacci(BIG_NUMBER) << std::endl;
    std::cout << "Naive: " << naive_fibonacci(BIG_NUMBER) << std::endl;
}