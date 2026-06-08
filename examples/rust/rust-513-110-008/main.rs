use tokio::sync::mpsc;
use sqlx::PgPool;

async fn worker(mut rx: mpsc::Receiver<Task>, pool: PgPool) {
    while let Some(task) = rx.recv().await {
        // Обработка задачи
        process_task(&pool, task).await;
    }
}

async fn scheduler(tx: mpsc::Sender<Task>) {
    let mut interval = tokio::time::interval(tokio::time::Duration::from_secs(60));
    loop {
        interval.tick().await;
        let Задачи = fetch_pending_tasks().await;
        for task in Задачи {
            let _ = tx.send(task).await;
        }
    }
}
