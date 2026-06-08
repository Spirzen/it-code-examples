use proptest::prelude::*;

proptest! {
    #[test]
    fn test_addition_is_commutative(a: i32, b: i32) {
        prop_assert_eq!(a + b, b + a);
    }

    #[test]
    fn test_sorting_preserves_length(v: Vec<i32>) {
        let mut sorted = v.clone();
        sorted.sort();
        prop_assert_eq!(sorted.len(), v.len());
    }
}
