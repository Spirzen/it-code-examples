class DataProcessor 
{
public:
    DataProcessor();
    ~DataProcessor();

    void load_data(const std::string& path);
    void process();
    void save_results(const std::string& output_path);

private:
    std::vector<DataRecord> records_;
    size_t processed_count_;
    std::mutex processing_mutex_;
};
