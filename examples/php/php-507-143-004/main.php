class UserPresenter
{
    protected $user;

    public function __construct(User $user)
    {
        $this->user = $user;
    }

    public function getFullName()
    {
        return $this->user->first_name . ' ' . $this->user->last_name;
    }
}
