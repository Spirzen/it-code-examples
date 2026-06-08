function parse_user_input(text)
  if not text or text == "" then
    return nil, "Input cannot be empty"
  end
  
  local number = tonumber(text)
  if not number then
    return nil, "Input must be a valid number"
  end
  
  return number, nil
end

local value, err = parse_user_input(user_text)
if err then
  show_error_message(err)
else
  process_value(value)
end
