function openDb() {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open('AppCache', 1);

    request.onupgradeneeded = (event) => {
      const db = event.target.result;
      if (!db.objectStoreNames.contains('articles')) {
        db.createObjectStore('articles', { keyPath: 'id' });
      }
    };

    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

async function saveArticle(article) {
  const db = await openDb();
  return new Promise((resolve, reject) => {
    const tx = db.transaction('articles', 'readwrite');
    tx.objectStore('articles').put(article);
    tx.oncomplete = () => resolve();
    tx.onerror = () => reject(tx.error);
  });
}
