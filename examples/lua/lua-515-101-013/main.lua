it("loads resource asynchronously", function()
  local completed = false
  local result = nil
  
  ResourceManager.load("texture.png", function(res)
    result = res
    completed = true
  end)
  
  -- ожидание завершения (в реальных тестах используйте фреймворк)
  while not completed do
    coroutine.yield()
  end
  
  assert.truthy(result)
  assert.equals("texture.png", result.name)
end)
