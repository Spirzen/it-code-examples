class MockStorage : public StorageInterface 
{
public:
    MOCK_METHOD(void, store, (const std::string&, const std::string&), (override));
    MOCK_METHOD(std::string, load, (const std::string&), (override));
    MOCK_METHOD(bool, exists, (const std::string&), (override));
    MOCK_METHOD(void, remove, (const std::string&), (override));
};

TEST(DocumentServiceTest, SavesDocumentToStorage) 
{
    auto mock_storage = std::make_unique<MockStorage>();
    EXPECT_CALL(*mock_storage, store("doc1", "content"))
        .Times(1);

    DocumentService service(std::move(mock_storage));
    service.save_document("doc1", "content");
}
