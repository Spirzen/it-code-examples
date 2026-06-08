-- network/http.lua
local http = {}

function http.get(url)
  ...
end

function http.post(url, body)
  ...
end

return http

-- main.lua
local http = require("network.http")
http.get("https://example.com")
