#include "math_utils.hpp"
#include <algorithm>
#include <cmath>

namespace math {
    double clamp(double value, double min, double max) {
        return std::max(min, std::min(value, max));
    }

    bool is_prime(int n) {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i <= std::sqrt(n); i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
