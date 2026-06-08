// Нарушение принципа
class UserAndDocumentManager 
{
public:
    void create_user();
    void delete_user();
    void save_document();
    void load_document();
};

// Корректная декомпозиция
class UserManager 
{
public:
    void create(const User& user);
    void remove(UserId id);
};

class DocumentStorage 
{
public:
    void save(const Document& doc);
    Document load(DocumentId id);
};
