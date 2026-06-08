use tokio::task;

async fn task_a() {
    println!("Task A");
}

async fn task_b() {
    println!("Task B");
}

#[tokio::main]
async fn main() {
    let handle_a = task::spawn(task_a());
    let handle_b = task::spawn(task_b());
    
    handle_a.await.unwrap();
    handle_b.await.unwrap();
}
