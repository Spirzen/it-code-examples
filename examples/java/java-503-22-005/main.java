// получение EntityManager (в Spring Boot — инъекция через @PersistenceContext)
@Transactional
public void transferFunds(Long fromId, Long toId, BigDecimal amount) {
    User from = em.find(User.class, fromId); // загружает сущность по ID
    User to = em.find(User.class, toId);

    if (from.getBalance().compareTo(amount) < 0) {
        throw new InsufficientFundsException();
    }

    from.setBalance(from.getBalance().subtract(amount));
    to.setBalance(to.getBalance().add(amount));

    // никаких em.update() не требуется!
    // изменения автоматически синхронизируются с БД при коммите транзакции (flush)
}
