class QueryBuilder
{
    protected $select = ['*'];
    protected $from;
    protected $where = [];
    protected $bindings = [];

    public function select($columns = ['*'])
    {
        $this->select = $columns;
        return $this;
    }

    public function from($table)
    {
        $this->from = $table;
        return $this;
    }

    public function where($column, $value)
    {
        $this->where[] = "$column = ?";
        $this->bindings[] = $value;
        return $this;
    }

    public function get()
    {
        // Генерация SQL и выполнение
        $sql = "SELECT " . implode(', ', $this->select) . " FROM " . $this->from;
        if ($this->where) {
            $sql .= " WHERE " . implode(' AND ', $this->where);
        }
        return DB::select($sql, $this->bindings);
    }
}
