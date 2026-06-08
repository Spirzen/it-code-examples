local function create_entity(config)
  local entity = {
    position = config.position or { x = 0, y = 0 },
    velocity = config.velocity or { x = 0, y = 0 },
    health = config.health or 100,
    tags = config.tags or {}
  }
  return entity
end

local enemy = create_entity({
  position = { x = 100, y = 200 },
  health = 150,
  tags = { "hostile", "ranged" }
})
