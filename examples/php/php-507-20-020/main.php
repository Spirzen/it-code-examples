interface UserRepositoryInterface
{
    public function findById(UserId $id): ?User;
    public function save(User $user): void;
}

class DoctrineUserRepository implements UserRepositoryInterface
{
    public function findById(UserId $id): ?User
    {
        // Использует Doctrine EntityManager
        return $this->em->find(User::class, $id->value());
    }

    public function save(User $user): void
    {
        $this->em->persist($user);
        $this->em->flush();
    }
}

// В CLI-задаче или миграции — можно подменить на SQLite-реализацию для тестов
