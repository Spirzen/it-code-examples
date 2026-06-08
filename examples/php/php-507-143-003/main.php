class UserObserver
{
    public function created(User $user)
    {
        Log::info('New user registered: ' . $user->email);
    }

    public function updating(User $user)
    {
        if ($user->isDirty('email')) {
            Notification::send($user, new EmailChanged());
        }
    }
}
