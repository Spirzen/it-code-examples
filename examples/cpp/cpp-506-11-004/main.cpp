bool isEven(int n) {
    return n % 2 == 0;
}

bool isValidPointer(const void* p) {
    return p != nullptr;
}

int main() {
    if (isEven(10)) {
        std::cout << "10 is even\n";
    }

    int* p = nullptr;
    if (!isValidPointer(p)) {
        std::cout << "Pointer is invalid\n";
    }

    return 0;
}
