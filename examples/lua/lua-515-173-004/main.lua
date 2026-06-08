local function fetch_data(url)
    if not url then
        error("URL is required")
    end
    return "payload"
end

local ok, data = pcall(fetch_data, nil)

if ok then
    print("Data:", data)
else
    print("Fetch failed, continuing:", data)
end
