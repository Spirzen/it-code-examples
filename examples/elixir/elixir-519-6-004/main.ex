defmodule MyApp.Feature do
  @moduledoc "Короткое описание модуля."

  @doc "Публичный вход в сценарий."
  @spec run(map()) :: {:ok, map()} | {:error, atom()}
  def run(input) when is_map(input) do
    with {:ok, normalized} <- normalize(input),
         {:ok, result} <- execute(normalized) do
      {:ok, result}
    end
  end

  defp normalize(input), do: {:ok, input}
  defp execute(data), do: {:ok, data}
end
