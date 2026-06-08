#pragma once

#include <string>
#include <vector>

namespace network {

class Connection 
{
public:
    explicit Connection(const std::string& address);
    ~Connection();

    bool connect();
    void disconnect();
    bool is_connected() const;

private:
    std::string address_;
    void* handle_;  // Системный дескриптор соединения
};

}  // namespace network
