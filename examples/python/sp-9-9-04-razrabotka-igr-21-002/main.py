   from mcpi.minecraft import Minecraft
   from mcpi import block
   import time

   # Подключение к локальному серверу
   mc = Minecraft.create(address="localhost", port=4711)

   # Получаем позицию игрока (целочисленную, "плиточную")
   pos = mc.player.getTilePos()
   mc.postToChat("Строим башню рядом с вами...")

   # Строим башню 5×5×10 из камня
   x, y, z = pos.x + 3, pos.y, pos.z
   width, height = 5, 10

   for dy in range(height):
       for dx in range(width):
           for dz in range(width):
               mc.setBlock(x + dx, y + dy, z + dz, block.STONE.id)

   mc.postToChat("Готово!")
