getUser
  .then((user) => {
    console.log("Пользователь:", user);
    return user.id;
  })
  .then((id) => {
    console.log("ID:", id);
  })
  .catch((error) => {
    console.error("Ошибка:", error.message);
  })
  .finally(() => {
    console.log("Готово!");
  });
