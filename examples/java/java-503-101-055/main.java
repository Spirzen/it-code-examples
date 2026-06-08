@Component
public class GracefulShutdown implements DisposableBean {
    private static final Logger logger = LoggerFactory.getLogger(GracefulShutdown.class);
    
    private final ExecutorService taskExecutor;
    private final MessageListenerContainer messageListener;
    private final long shutdownTimeoutMillis = 30_000;
    
    @Override
    public void destroy() {
        logger.info("Начало корректного завершения работы");
        
        // Остановка приёма новых сообщений
        if (messageListener != null) {
            messageListener.stop();
            logger.info("Приём сообщений остановлен");
        }
        
        // Завершение выполняющихся задач
        taskExecutor.shutdown();
        try {
            if (!taskExecutor.awaitTermination(shutdownTimeoutMillis, TimeUnit.MILLISECONDS)) {
                logger.warn("Не все задачи завершились за {} мс, принудительная остановка", shutdownTimeoutMillis);
                List<Runnable> dropped = taskExecutor.shutdownNow();
                logger.warn("Принудительно остановлено {} задач", dropped.size());
            } else {
                logger.info("Все задачи успешно завершены");
            }
        } catch (InterruptedException e) {
            logger.warn("Ожидание завершения прервано", e);
            taskExecutor.shutdownNow();
            Thread.currentThread().interrupt();
        }
        
        logger.info("Завершение работы приложения завершено");
    }
}
