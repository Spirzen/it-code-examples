#include <string>
#include <vector>
#include <chrono>
#include <optional>
#include <cstdint>

// Строгое перечисление — безопасное именование режимов
enum class Protocol : uint8_t {
    HTTP,
    HTTPS,
    WebSocket
};

// Агрегатная структура: данные без логики, инициализируется списком
struct Endpoint {
    std::string host;
    uint16_t port;
    Protocol proto;
};

// Класс с инкапсуляцией и управлением состоянием
class ServiceConfig {
    std::string name_;
    std::vector<Endpoint> endpoints_;
    std::chrono::seconds timeout_;
    mutable std::optional<size_t> hash_cache_; // кэш хеша — изменяем в const-методах

public:
    // Конструктор с проверкой инварианта
    ServiceConfig(
        std::string name,
        std::vector<Endpoint> endpoints,
        int timeout_sec
    )
        : name_(std::move(name))
        , endpoints_(std::move(endpoints))
        , timeout_(std::chrono::seconds{timeout_sec})
    {
        if (name_.empty()) throw std::invalid_argument("name must not be empty");
        if (endpoints_.empty()) throw std::invalid_argument("at least one endpoint required");
        if (timeout_sec <= 0) throw std::invalid_argument("timeout must be positive");
    }

    // Доступ только для чтения через константные ссылки
    const std::string& name() const { return name_; }
    const std::vector<Endpoint>& endpoints() const { return endpoints_; }
    std::chrono::seconds timeout() const { return timeout_; }

    // Хеширование с кэшированием — mutable позволяет модифицировать cache в const-контексте
    size_t hash() const {
        if (!hash_cache_) {
            size_t h = std::hash<std::string>{}(name_);
            for (const auto& ep : endpoints_) {
                // Простой комбинированный хеш
                h ^= std::hash<std::string>{}(ep.host) + 0x9e3779b9
                   ^ (ep.port << 16)
                   ^ static_cast<size_t>(ep.proto);
            }
            hash_cache_ = h;
        }
        return *hash_cache_;
    }

    // Оператор равенства — значение-ориентированное сравнение
    bool operator==(const ServiceConfig& other) const {
        return name_ == other.name_
            && endpoints_ == other.endpoints_
            && timeout_ == other.timeout_;
    }
};
