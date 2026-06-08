-- файл: utils/string.lua
local String = {}

function String.trim(text)
  return text:match("^%s*(.-)%s*$")
end

function String.split(text, delimiter)
  local result = {}
  for match in (text .. delimiter):gmatch("(.-)" .. delimiter) do
    table.insert(result, match)
  end
  return result
end

return String
