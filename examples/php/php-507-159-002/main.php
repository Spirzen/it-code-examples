try {
    processOrder($id);
} catch (\PDOException $e) {
    // База недоступна — отдельная ветка
    logError('db', $e);
    showServiceUnavailable();
} catch (\TypeError $e) {
    // Ошибка типов — чаще баг в коде
    logError('bug', $e);
    throw $e; // проброс после логирования
} catch (\Throwable $e) {
    logError('general', $e);
    showGenericError();
}
