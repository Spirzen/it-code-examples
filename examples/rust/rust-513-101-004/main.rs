use tokio::sync::Semaphore;
use std::sync::Arc;

async fn process_batch(urls: Vec<String>) -> Vec<Result<Vec<u8>, reqwest::Error>> {
    let semaphore = Arc::new(Semaphore::new(10));
    let mut handles = Vec::new();
    
    for url in urls {
        let permit = semaphore.clone().acquire_owned().await.unwrap();
        let handle = tokio::spawn(async move {
            let result = fetch_data(&url).await;
            drop(permit); // освобождаем слот семафора
            result
        });
        handles.push(handle);
    }
    
    futures::future::join_all(handles).await
}
