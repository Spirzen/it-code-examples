defmodule Greet do
  @doc """
  Возвращает приветствие для заданного имени.

  ## Параметры

  - `name`: строка, представляющая имя человека.

  ## Примеры

      iex> Greet.hello("Мир")
      "Привет, Мир!"

  """
  def hello(name) when is_binary(name) do
    "Привет, #{name}!"
  end
end
