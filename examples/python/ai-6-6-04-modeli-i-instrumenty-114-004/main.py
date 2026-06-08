from modelcontextprotocol import MCPClient

async def main():
    async with MCPClient('http://localhost:3000') as client:
        # Подключение и получениеcapabilities
        capabilities = await client.initialize()
        print("Capabilities:", capabilities)
        
        # Список ресурсов
        resources = await client.list_resources()
        print("Resources:", resources)
        
        # Чтение файла
        log_content = await client.read_resource("file:///var/log/app.log")
        print("Log:", log_content[:500])
        
        # Вызов инструмента
        disk_result = await client.call_tool(
            "check_disk_space",
            {"path": "/data"}
        )
        print("Disk Status:", disk_result)

import asyncio

asyncio.run(main())
