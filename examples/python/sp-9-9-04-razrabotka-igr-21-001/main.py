
import asyncio

from mcapi import AsyncMinecraft

async def main():
    mc = await AsyncMinecraft.connect()
    world = await mc.getWorld()
    chunk = await world.getChunk(0, 0)
    # Анализ высоты поверхности в чанке
    heights = [max(y for y in range(256) if chunk.getBlock(x, y, z) != 0)
               for x in range(16) for z in range(16)]
    await mc.postToChat(f"Средняя высота: {sum(heights)/len(heights):.1f}")
    await mc.close()

asyncio.run(main())
