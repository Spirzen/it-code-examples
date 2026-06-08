function xhrGet(url) {
  return new Promise((resolve, reject) => {
    const req = new XMLHttpRequest();
    req.open('GET', url);
    req.responseType = 'json';
    req.onload = () => {
      if (req.status >= 200 && req.status < 300) {
        resolve(req.response);
      } else {
        reject(new Error(`HTTP ${req.status}`));
      }
    };
    req.onerror = () => reject(new Error('Network error'));
    req.send();
  });
}
