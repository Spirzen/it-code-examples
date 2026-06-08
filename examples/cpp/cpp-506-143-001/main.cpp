class HashTable {
public:
    class Iterator {
        HashTable* table_;
        size_t index_;
        friend class HashTable;
        Iterator(HashTable* t, size_t i) : table_(t), index_(i) {}
    public:
        bool operator!=(const Iterator& other) const {
            return index_ != other.index_;
        }
    };
    Iterator begin();
    Iterator end();
};
