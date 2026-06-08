let cachedData = null;

function getData() {
  if (cachedData) {
    return Promise.resolve(cachedData); // Немедленный успех
  }
  return fetch("/api/data")
    .then((data) => {
      cachedData = data; // Кешируем
      return data;
    });
}

getData().then((data) => console.log(data));
