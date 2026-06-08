function table_shallow_copy(original)
  local copy = {}
  for key, value in pairs(original) do
    copy[key] = value
  end
  return copy
end

function table_deep_copy(original)
  local copy = {}
  for key, value in pairs(original) do
    if type(value) == "table" then
      copy[key] = table_deep_copy(value)
    else
      copy[key] = value
    end
  end
  return copy
end
