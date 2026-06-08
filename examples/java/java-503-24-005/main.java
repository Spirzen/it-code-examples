// ArrayList
List<String> list = new ArrayList<>();
list.add("Java");
list.add(0, "Hello"); // вставка в начало
System.out.println(list.get(1)); // Java

// HashSet
Set<Integer> uniqueNumbers = new HashSet<>();
uniqueNumbers.add(1);
uniqueNumbers.add(1); // дубликат игнорируется
System.out.println(uniqueNumbers.contains(1)); // true

// HashMap
Map<String, Integer> scores = new HashMap<>();
scores.put("Alice", 90);
System.out.println(scores.get("Alice")); // 90

// PriorityQueue
Queue<Integer> queue = new PriorityQueue<>();
queue.offer(5);
queue.offer(3);
System.out.println(queue.poll()); // 3 (минимальный элемент)
