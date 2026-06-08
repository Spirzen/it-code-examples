# Пример простой логики кластера
class ClusterNode:
    def __init__(self, node_id, status='active'):
        self.node_id = node_id
        self.status = status
    
    def handle_request(self, request):
        if self.status == 'active':
            return process(request)
        return None

# Мониторинг состояния узлов
nodes = [ClusterNode(i) for i in range(5)]
for node in nodes:
    print(f"Node {node.node_id}: {node.status}")
