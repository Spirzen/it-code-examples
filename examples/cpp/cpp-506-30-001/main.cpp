using FilePtr = std::unique_ptr<std::FILE, decltype(&std::fclose)>;

FilePtr open_file(const char* path, const char* mode) {
    return FilePtr(std::fopen(path, mode), &std::fclose);
}

void load_config(const char* path) {
    auto f = open_file(path, "rb");
    if (!f) return;

    do_work(f.get());

    if (something_bad()) return; // std::fclose через deleter
}
