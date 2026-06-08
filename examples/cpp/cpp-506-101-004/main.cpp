#include "network_connection.hpp"

#include <stdexcept>
#include <system_error>

#include "internal/socket_utils.hpp"

namespace network {

Connection::Connection(const std::string& address)
    : address_(address), handle_(nullptr) 
{
    // Инициализация
}

// Реализация методов...

}  // namespace network
