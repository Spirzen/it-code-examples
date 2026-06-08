#include <fcntl.h>
#include <stdexcept>
#include <string>
#include <unistd.h>

class FileDescriptor {
public:
    explicit FileDescriptor(const std::string& path) {
        fd_ = ::open(path.c_str(), O_RDONLY);
        if (fd_ == -1) {
            throw std::runtime_error("open failed");
        }
    }

    ~FileDescriptor() {
        if (fd_ != -1) {
            ::close(fd_);
        }
    }

    FileDescriptor(const FileDescriptor&) = delete;
    FileDescriptor& operator=(const FileDescriptor&) = delete;

    int get() const { return fd_; }

private:
    int fd_ = -1;
};
