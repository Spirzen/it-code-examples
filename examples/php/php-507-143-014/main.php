class CacheManager
{
    protected $app;
    protected $stores = [];

    public function store($name = null)
    {
        $name = $name ?: $this->getDefaultDriver();
        if (!isset($this->stores[$name])) {
            $this->stores[$name] = $this->resolve($name);
        }
        return $this->stores[$name];
    }

    protected function resolve($name)
    {
        $config = $this->getConfig($name);
        return $this->createAdapter($config['driver'], $config);
    }
}
