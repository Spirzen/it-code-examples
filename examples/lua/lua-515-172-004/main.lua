function process_large_file(input_file, output_file)
    local input = io.open(input_file, "r")
    local output = io.open(output_file, "w")
    
    if not input or not output then
        if input then input:close() end
        if output then output:close() end
        return false
    end
    
    for line in input:lines() do
        local processed = string.gsub(line, "%s+", " ")
        output:write(processed, "\n")
    end
    
    input:close()
    output:close()
    return true
end

process_large_file("input.log", "output.log")
