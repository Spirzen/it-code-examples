// Правильно: await в try
async function save() {
  try {
    await db.insert(row);
  } catch (e) {
    logger.error(e);
    throw e;
  }
}

// Ошибка: забыли await — rejection уйдёт мимо try
async function broken() {
  try {
    db.insert(row); // Promise без await
  } catch (e) {
    /* сюда не попадём при reject */
  }
}
