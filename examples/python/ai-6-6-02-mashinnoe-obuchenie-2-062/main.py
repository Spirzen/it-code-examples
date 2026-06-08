
import torch
import torch.nn.functional as F

from torch_geometric.nn import GCNConv, GATConv, SAGEConv
from torch_geometric.data import Data

import numpy as np
import matplotlib.pyplot as plt

# Генерация синтетического графа с сообществами
def generate_community_graph(n_nodes=200, n_communities=4, p_in=0.1, p_out=0.01):
    # Инициализация матрицы смежности
    adj = np.zeros((n_nodes, n_nodes))
    
    # Создание сообществ
    community_size = n_nodes // n_communities
    for comm in range(n_communities):
        start = comm * community_size
        end = start + community_size if comm < n_communities - 1 else n_nodes
        
        # Плотные связи внутри сообщества
        for i in range(start, end):
            for j in range(i + 1, end):
                if np.random.rand() < p_in:
                    adj[i, j] = adj[j, i] = 1
    
    # Разреженные связи между сообществами
    for i in range(n_nodes):
        for j in range(i + 1, n_nodes):
            if adj[i, j] == 0 and np.random.rand() < p_out:
                adj[i, j] = adj[j, i] = 1
    
    # Создание списка рёбер
    edge_index = []
    for i in range(n_nodes):
        for j in range(i + 1, n_nodes):
            if adj[i, j] == 1:
                edge_index.append([i, j])
                edge_index.append([j, i])  # неориентированный граф
    
    edge_index = torch.tensor(edge_index, dtype=torch.long).t().contiguous()
    
    # Признаки узлов — координаты в пространстве сообществ
    x = torch.zeros(n_nodes, n_communities)
    for node in range(n_nodes):
        comm = node // community_size
        x[node, comm] = 1.0
    
    # Метки классов — номер сообщества
    y = torch.tensor([node // community_size for node in range(n_nodes)], dtype=torch.long)
    
    return Data(x=x, edge_index=edge_index, y=y), n_communities

# Создание синтетического графа
graph_data, n_communities = generate_community_graph(n_nodes=300, n_communities=5)
print(f"Граф содержит {data.num_nodes} узлов и {data.edge_index.size(1) // 2} рёбер")

# Базовая графовая свёрточная сеть
class GCN(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super(GCN, self).__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, out_channels)
    
    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = F.dropout(x, p=0.5, training=self.training)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

# Сеть с механизмом внимания
class GAT(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels, heads=4):
        super(GAT, self).__init__()
        self.conv1 = GATConv(in_channels, hidden_channels, heads=heads, dropout=0.6)
        self.conv2 = GATConv(hidden_channels * heads, out_channels, heads=1, concat=False, dropout=0.6)
    
    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.elu(x)
        x = F.dropout(x, p=0.5, training=self.training)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

# Сеть GraphSAGE
class GraphSAGE(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels, out_channels):
        super(GraphSAGE, self).__init__()
        self.conv1 = SAGEConv(in_channels, hidden_channels)
        self.conv2 = SAGEConv(hidden_channels, out_channels)
    
    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = F.dropout(x, p=0.5, training=self.training)
        x = self.conv2(x, edge_index)
        return F.log_softmax(x, dim=1)

# Разделение узлов на обучающие, валидационные и тестовые
def split_nodes(num_nodes, train_ratio=0.6, val_ratio=0.2):
    indices = torch.randperm(num_nodes)
    train_end = int(num_nodes * train_ratio)
    val_end = train_end + int(num_nodes * val_ratio)
    
    train_mask = torch.zeros(num_nodes, dtype=torch.bool)
    val_mask = torch.zeros(num_nodes, dtype=torch.bool)
    test_mask = torch.zeros(num_nodes, dtype=torch.bool)
    
    train_mask[indices[:train_end]] = True
    val_mask[indices[train_end:val_end]] = True
    test_mask[indices[val_end:]] = True
    
    return train_mask, val_mask, test_mask

data.train_mask, data.val_mask, data.test_mask = split_nodes(data.num_nodes)

# Обучение и сравнение архитектур
def train_model(model, graph_data, epochs=200):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)
    data = data.to(device)
    
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=5e-4)
    
    train_losses = []
    val_accuracies = []
    
    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        out = model(data.x, data.edge_index)
        loss = F.nll_loss(out[data.train_mask], data.y[data.train_mask])
        loss.backward()
        optimizer.step()
        train_losses.append(loss.item())
        
        model.eval()
        with torch.no_grad():
            out = model(data.x, data.edge_index)
            pred = out.argmax(dim=1)
            correct = pred[data.val_mask].eq(data.y[data.val_mask]).sum().item()
            acc = correct / data.val_mask.sum().item()
            val_accuracies.append(acc)
    
    return model, train_losses, val_accuracies

# Обучение трёх архитектур
print("Обучение графовых нейронных сетей...")
gcn_model, gcn_losses, gcn_accs = train_model(
    GCN(data.num_features, 64, n_communities), graph_data
)
gat_model, gat_losses, gat_accs = train_model(
    GAT(data.num_features, 16, n_communities, heads=4), graph_data
)
sage_model, sage_losses, sage_accs = train_model(
    GraphSAGE(data.num_features, 64, n_communities), graph_data
)

# Оценка качества на тестовой выборке
def evaluate_model(model, graph_data):
    model.eval()
    with torch.no_grad():
        out = model(data.x, data.edge_index)
        pred = out.argmax(dim=1)
        correct = pred[data.test_mask].eq(data.y[data.test_mask]).sum().item()
        acc = correct / data.test_mask.sum().item()
        return acc

gcn_test_acc = evaluate_model(gcn_model, graph_data)
gat_test_acc = evaluate_model(gat_model, graph_data)
sage_test_acc = evaluate_model(sage_model, graph_data)

print(f"\nТочность на тестовой выборке:")
print(f"GCN:  {gcn_test_acc:.2%}")
print(f"GAT:  {gat_test_acc:.2%}")
print(f"SAGE: {sage_test_acc:.2%}")

# Визуализация процесса обучения
plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
plt.plot(gcn_losses, label='GCN', alpha=0.8)
plt.plot(gat_losses, label='GAT', alpha=0.8)
plt.plot(sage_losses, label='GraphSAGE', alpha=0.8)
plt.xlabel('Эпоха')
plt.ylabel('Потери обучения')
plt.title('Динамика потерь обучения')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(gcn_accs, label='GCN', alpha=0.8)
plt.plot(gat_accs, label='GAT', alpha=0.8)
plt.plot(sage_accs, label='GraphSAGE', alpha=0.8)
plt.xlabel('Эпоха')
plt.ylabel('Точность на валидации')
plt.title('Динамика точности на валидации')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('gnn_training_dynamics.png')
plt.close()

# Визуализация вложений узлов после обучения
from sklearn.manifold import TSNE

def visualize_embeddings(model, graph_data, title):
    model.eval()
    with torch.no_grad():
        out = model(data.x, data.edge_index)
        embeddings = out.cpu().numpy()
    
    # Уменьшение размерности для визуализации
    tsne = TSNE(n_components=2, random_state=42, perplexity=30)
    embeddings_2d = tsne.fit_transform(embeddings)
    
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(
        embeddings_2d[:, 0], 
        embeddings_2d[:, 1],
        c=data.y.cpu().numpy(),
        cmap='tab10',
        alpha=0.8,
        s=50
    )
    plt.colorbar(scatter, label='Сообщество')
    plt.title(title)
    plt.xlabel('t-SNE компонента 1')
    plt.ylabel('t-SNE компонента 2')
    plt.grid(True, alpha=0.3)
    plt.savefig(f'gnn_embeddings_{title.replace(" ", "_").lower()}.png')
    plt.close()

visualize_embeddings(gcn_model, graph_data, 'Вложения узлов (GCN)')
visualize_embeddings(gat_model, graph_data, 'Вложения узлов (GAT)')
visualize_embeddings(sage_model, graph_data, 'Вложения узлов (GraphSAGE)')
