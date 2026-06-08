use std::collections::HashMap;

let mut scores = Vec::new();
scores.push(10);
scores.push(20);
scores.push(30);

let second = scores[1]; // 20
println!("Второй элемент: {}", second);

let mut users = HashMap::new();
users.insert("alice", 101);
users.insert("bob", 202);

if let Some(id) = users.get("alice") {
    println!("ID alice: {}", id);
}
