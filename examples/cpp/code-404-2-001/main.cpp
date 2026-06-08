// math.ixx (implementation unit)
export module math;

export int add(int a, int b) {
    return a + b;
}

// main.cpp

import math;

int main() {
    return add(2, 2); // → 4
}
