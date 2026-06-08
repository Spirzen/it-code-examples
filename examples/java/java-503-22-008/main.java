public class UserSpecs {
    public static Specification<User> hasStatus(Status status) {
        return (root, query, cb) -> cb.equal(root.get("status"), status);
    }

    public static Specification<User> balanceGreaterThan(BigDecimal amount) {
        return (root, query, cb) -> cb.greaterThan(root.get("balance"), amount);
    }
}

// Использование
userRepository.findAll(
    where(hasStatus(Status.ACTIVE)).and(balanceGreaterThan(BigDecimal.valueOf(1000)))
);
