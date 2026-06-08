  class QueryBuilder
    def initialize(&block)
      @clauses = []
      instance_eval(&block) if block
    end

    def where(condition)
      @clauses << condition
    end

    def to_sql
      "SELECT * WHERE #{ @clauses.join(' AND ') }"
    end
  end

  qb = QueryBuilder.new { where('a > 1'); where('b = 2') }
  qb.to_sql  # => "SELECT * WHERE a > 1 AND b = 2"
