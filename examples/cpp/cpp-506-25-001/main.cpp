#include <iostream>
#include <string>
#include <boost/asio.hpp>

int main() {
    try {
        boost::asio::io_context io;
        boost::asio::ip::tcp::resolver resolver(io);
        boost::asio::ip::tcp::socket socket(io);

        auto endpoints = resolver.resolve("example.com", "80");
        boost::asio::connect(socket, endpoints);

        const std::string request =
            "GET / HTTP/1.1\r\n"
            "Host: example.com\r\n"
            "Connection: close\r\n\r\n";
        boost::asio::write(socket, boost::asio::buffer(request));

        boost::asio::streambuf response;
        boost::system::error_code ec;
        while (boost::asio::read(socket, response, boost::asio::transfer_at_least(1), ec)) {}

        if (ec != boost::asio::error::eof && ec) {
            throw boost::system::system_error(ec);
        }

        std::cout << &response;
    } catch (const std::exception& ex) {
        std::cerr << "network error: " << ex.what() << '\n';
        return 1;
    }
}
