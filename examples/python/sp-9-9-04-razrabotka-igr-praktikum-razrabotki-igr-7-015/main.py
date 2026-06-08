import random
import settings


class MapNode:
    def __init__(self, node_type: str, floor: int, row: int):
        self.type = node_type
        self.floor = floor
        self.row = row
        self.connections: list["MapNode"] = []
        self.available = False
        self.completed = False

    @property
    def color(self):
        return settings.NODE_COLORS.get(self.type, (120, 120, 120))


class GameMap:
    FLOORS = 8  # в практикуме короче, в эталоне 15

    def __init__(self):
        self.floors: list[list[MapNode]] = []
        self.current_node: MapNode | None = None
        self._generate()

    def _generate(self):
        for f in range(self.FLOORS):
            row = random.randint(0, 2)
            ntype = settings.NODE_BOSS if f == self.FLOORS - 1 else settings.NODE_COMBAT
            if f > 0 and f % 4 == 0:
                ntype = settings.NODE_REST
            self.floors.append([MapNode(ntype, f, row)])
        for f in range(len(self.floors) - 1):
            for a in self.floors[f]:
                for b in self.floors[f + 1]:
                    if abs(a.row - b.row) <= 1:
                        a.connections.append(b)
        for node in self.floors[0]:
            node.available = True

    def select_node(self, node: MapNode) -> bool:
        if not node.available or node.completed:
            return False
        if self.current_node and node not in self.current_node.connections:
            if node.floor != 0:
                return False
        self.current_node = node
        node.completed = True
        for n in self._all_nodes():
            n.available = False
        for nxt in node.connections:
            nxt.available = True
        return True

    def _all_nodes(self):
        for floor in self.floors:
            for n in floor:
                yield n
