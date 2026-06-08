#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    #[should_panic]
    fn this_panics() {
        panic!("Oops!");
    }

    #[test]
    #[ignore]
    fn expensive_test() {
        // пропускается при обычном `cargo test`
    }
}
