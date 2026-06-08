template<typename StoragePolicy, typename LoggingPolicy>
class Container : private StoragePolicy, private LoggingPolicy {
public:
    void add(int value) {
        StoragePolicy::store(value);
        LoggingPolicy::log("Added", value);
    }
};

struct VectorStorage {
    std::vector<int> data;
    void store(int v) { data.push_back(v); }
};

struct SilentLogging {
    void log(const char*, int) {}
};

using MyContainer = Container<VectorStorage, SilentLogging>;
