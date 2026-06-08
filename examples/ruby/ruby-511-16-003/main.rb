MAX_RETRIES = 3
retries = 0

begin
  User.transaction do
    user = User.lock.find(42)
    user.balance_cents -= 500
    user.save!
  end
rescue ActiveRecord::Deadlocked, ActiveRecord::SerializationFailure
  retries += 1
  raise if retries > MAX_RETRIES
  sleep(0.05 * retries)
  retry
end
