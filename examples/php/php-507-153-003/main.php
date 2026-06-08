class UserCollection implements IteratorAggregate {
    private array $users = [];

    public function add(User $user): void {
        $this->users[] = $user;
    }

    public function getAdmins(): UserCollection {
        $admins = new UserCollection();
        foreach ($this->users as $user) {
            if ($user->hasRole('admin')) {
                $admins->add($user);
            }
        }
        return $admins;
    }

    public function getIterator(): Traversable {
        return new ArrayIterator($this->users);
    }
}
