defmodule EchoServer do
  def start do
    spawn(&loop/0)
  end

  defp loop do
    receive do
      {:echo, msg, caller} ->
        send(caller, {:reply, msg})
        loop()  # Рекурсивный вызов для продолжения работы
      :stop ->
        IO.puts("Сервер остановлен")
        # Без рекурсивного вызова — процесс завершается
    end
  end
end

# Использование —
server = EchoServer.start()
send(server, {:echo, "Привет!", self()})
receive do
  {:reply, msg} -> IO.puts("Получено: #{msg}")
end
