interface CacheStore
{
    public function get($key);
    public function put($key, $value, $seconds);
}

class RedisAdapter implements CacheStore
{
    protected $redis;

    public function __construct(RedisClient $redis)
    {
        $this->redis = $redis;
    }

    public function get($key)
    {
        return $this->redis->get($key);
    }

    public function put($key, $value, $seconds)
    {
        $this->redis->setex($key, $seconds, $value);
    }
}
