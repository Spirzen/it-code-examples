# if — бинарная развилка
if score > 50 do
  :pass
else
  :fail
end

# cond — несколько независимых условий
cond do
  score >= 90 -> :excellent
  score >= 70 -> :good
  score >= 50 -> :pass
  true -> :fail
end

# case — выбор по форме данных
case response do
  {:ok, data} -> {:ok, data}
  {:error, reason} -> {:error, reason}
end
