defmodule Counter do
  def start, do: spawn(fn -> loop(0) end)

  defp loop(n) do
    receive do
      :inc -> loop(n + 1)
      {:get, pid} -> send(pid, n); loop(n)
    end
  end
end

pid = Counter.start()
send(pid, :inc)
send(pid, {:get, self()})
receive do: n when is_integer(n) -> IO.inspect(n)
