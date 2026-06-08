pub trait RandomGenerator {
    type Output;

    fn generate(&self) -> Self::Output;
}

pub struct IntegerGenerator;
pub struct StringGenerator;

impl RandomGenerator for IntegerGenerator {
    type Output = i32;

    fn generate(&self) -> i32 {
        rand::random()
    }
}

impl RandomGenerator for StringGenerator {
    type Output = String;

    fn generate(&self) -> String {
        "random_string".to_string()
    }
}
