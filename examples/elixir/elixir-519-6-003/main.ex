defmodule Counter do
  use GenServer

  def start_link(initial_value) do
    GenServer.start_link(__MODULE__, initial_value, name: __MODULE__)
  end

  def increment(amount) do
    GenServer.cast(__MODULE__, {:increment, amount})
  end

  def value do
    GenServer.call(__MODULE__, :value)
  end

  # Callback-функции
  def init(initial_value), do: {:ok, initial_value}

  def handle_cast({:increment, amount}, state) do
    {:noreply, state + amount}
  end

  def handle_call(:value, _from, state) do
    {:reply, state, state}
  end
end

# Запуск и использование —
Counter.start_link(0)
Counter.increment(5)
Counter.increment(3)
IO.puts(Counter.value())  # Выведет: 8
