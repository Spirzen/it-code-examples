const { MCPCoreClient } = require('@modelcontextprotocol/client');

async function connect() {
  const client = new MCPCoreClient('ws://localhost:3000');
  
  await client.connect();
  
  // Получение списка доступных ресурсов
  const resources = await client.listResources();
  console.log('Доступные ресурсы:', resources);
  
  // Чтение контента
  const content = await client.readResource({
    uri: 'file:///var/log/app.log'
  });
  
  console.log('Содержимое:', content);
  
  // Вызов инструмента
  const result = await client.callTool({
    name: 'checkDiskSpace',
    arguments: { path: '/data' }
  });
  
  console.log('Результат:', result);
  
  await client.close();
}

connect().catch(console.error);
