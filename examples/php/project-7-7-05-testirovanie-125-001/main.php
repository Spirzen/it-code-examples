class UserFilterAge
{
    const AGE_THRESHOLD = 18;

    public function __invoke(array $collection)
    {
        return array_filter(
            $collection,
            function (array $item) {
                return $item['age'] >= self::AGE_THRESHOLD;
            }
        );
    }
}
