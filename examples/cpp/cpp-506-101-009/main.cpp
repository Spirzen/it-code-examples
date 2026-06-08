class StorageInterface 
{
public:
    virtual ~StorageInterface() = default;

    virtual void store(const std::string& key, const std::string& value) = 0;
    virtual std::string load(const std::string& key) = 0;
    virtual bool exists(const std::string& key) = 0;
    virtual void remove(const std::string& key) = 0;
};

class InMemoryStorage : public StorageInterface 
{
public:
    void store(const std::string& key, const std::string& value) override;
    std::string load(const std::string& key) override;
    bool exists(const std::string& key) override;
    void remove(const std::string& key) override;

private:
    std::unordered_map<std::string, std::string> data_;
};
