local Vector2Pool = {
  _pool = {},
  _index = 0
}

function Vector2Pool.acquire(x, y)
  local vec
  if self._index > 0 then
    vec = self._pool[self._index]
    self._index = self._index - 1
  else
    vec = { x = 0, y = 0 }
  end
  vec.x = x or 0
  vec.y = y or 0
  return vec
end

function Vector2Pool.release(vec)
  self._index = self._index + 1
  self._pool[self._index] = vec
end
