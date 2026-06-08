// Шаг 1: инициализация — каждому узлу — свой "label"
MATCH (n:User)
SET n.temp_label = id(n)

// Шаг 2: итеративно обновлять метку → мода соседей
// (выполняется N раз вручную или через APOC)
CALL apoc.periodic.iterate(
  "MATCH (n:User) RETURN n",
  "MATCH (n)-[:FRIENDS]-(f)
   WITH n, apoc.coll.frequencies([f IN collect(f) | f.temp_label]) AS freqs
   WITH n, reduce(m = {label: null, count: 0}, item IN freqs |
     CASE WHEN item.count > m.count THEN {label: item.item, count: item.count} ELSE m END
   ).label AS new_label
   SET n.temp_label = new_label",
  {batchSize: 1000, parallel: true}
)
YIELD batches, total
RETURN batches, total
