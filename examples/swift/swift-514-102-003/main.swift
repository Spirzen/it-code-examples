class MathUtilities {
    class func calculateFactorial(of number: Int) -> Int {
        guard number > 1 else { return 1 }
        return number * calculateFactorial(of: number - 1)
    }
    
    static func isPrime(_ number: Int) -> Bool {
        guard number > 1 else { return false }
        for i in 2..<number {
            if number % i == 0 {
                return false
            }
        }
        return true
    }
}
