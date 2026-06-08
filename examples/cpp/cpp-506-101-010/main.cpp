// Единственное владение
auto connection = std::make_unique<NetworkConnection>(endpoint);

// Совместное владение
std::shared_ptr<Document> shared_doc = std::make_shared<Document>(content);

// Избегание циклических ссылок
class Node 
{
public:
    void set_parent(std::weak_ptr<Node> parent) { parent_ = parent; }
    std::shared_ptr<Node> get_parent() { return parent_.lock(); }

private:
    std::weak_ptr<Node> parent_;
    std::vector<std::shared_ptr<Node>> children_;
};
