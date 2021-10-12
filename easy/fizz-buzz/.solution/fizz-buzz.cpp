#include <iostream>
template <unsigned int FIZZ = 3, unsigned int BUZZ = 5>
void fizzbuzz(int n) {
    unsigned int unsigned_n = n;
    for(unsigned int i = 1; i <= unsigned_n; ++i) {
        if(i % (FIZZ * BUZZ) == 0) {
            std::cout << "fizzbuzz";
        } else if (i % FIZZ == 0) {
            std::cout << "fizz";
        } else if (i % BUZZ == 0) {
            std::cout << "buzz";
        } else {
            std::cout << i;
        }
        std::cout << std::endl;
    }
}