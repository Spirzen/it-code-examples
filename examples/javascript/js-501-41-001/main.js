if (!navigator.geolocation) {
  console.warn('Геолокация не поддерживается');
  return;
}

navigator.geolocation.getCurrentPosition(
  (pos) => {
    const { latitude, longitude, accuracy } = pos.coords;
    console.log(latitude, longitude, `±${accuracy} м`);
  },
  (error) => {
    // 1 — отказ, 2 — ошибка устройства, 3 — timeout
    console.error(error.code, error.message);
  },
  {
    enableHighAccuracy: true,
    maximumAge: 10_000,
    timeout: 5_000,
  },
);
