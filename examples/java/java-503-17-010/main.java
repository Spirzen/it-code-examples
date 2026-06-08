class SharedBuffer {
    private String content;
    private boolean empty = true;
    
    public synchronized String read() {
        while (empty) {
            try {
                wait();  // ожидание, пока буфер не станет непустым
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        empty = true;
        notifyAll();  // уведомление ожидающих потоков записи
        return content;
    }
    
    public synchronized void write(String content) {
        while (!empty) {
            try {
                wait();  // ожидание, пока буфер не станет пустым
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        this.content = content;
        empty = false;
        notifyAll();  // уведомление ожидающих потоков чтения
    }
}
