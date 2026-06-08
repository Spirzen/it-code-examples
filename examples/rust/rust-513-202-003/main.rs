use mockall::automock;
use mockall::predicate::*;

#[automock]
trait Store {
    fn get(&self, id: u32) -> Option<String>;
}

#[test]
fn uses_mock_store() {
    let mut mock = MockStore::new();
    mock.expect_get()
        .with(eq(1))
        .times(1)
        .returning(|_| Some("заметка".into()));

    assert_eq!(Some("заметка".into()), mock.get(1));
}
