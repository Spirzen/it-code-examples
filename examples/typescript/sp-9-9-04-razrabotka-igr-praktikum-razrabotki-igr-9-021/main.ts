import {
  NODE_COMBAT,
  NODE_ELITE,
  NODE_BOSS,
  NODE_REST,
  NODE_SHOP,
  NODE_TREASURE,
  NODE_EVENT,
} from './settings';

export class MapNode {
  type: string;
  floor: number;
  col: number;
  row: number;
  connections: MapNode[] = [];
  visited = false;
  available = false;
  completed = false;

  constructor(nodeType: string, floor: number, col: number, row: number) {
    this.type = nodeType;
    this.floor = floor;
    this.col = col;
    this.row = row;
  }
}

export class GameMap {
  static FLOORS = 15;
  static ROWS_PER_FLOOR = 3;

  floors: MapNode[][] = [];
  currentNode: MapNode | null = null;

  constructor() {
    this.generate();
  }

  generate() {
    // Упрощённая генерация — полная версия в эталоне map.ts
    this.floors = [];
    for (let f = 0; f < GameMap.FLOORS; f++) {
      const count = f === 0 || f === GameMap.FLOORS - 1 ? 1 : 2 + Math.floor(Math.random() * 2);
      const floorNodes: MapNode[] = [];
      for (let i = 0; i < count; i++) {
        let ntype = NODE_COMBAT;
        if (f === GameMap.FLOORS - 1) ntype = NODE_BOSS;
        else if (f > 0 && f % 5 === 0 && i === 0) ntype = NODE_REST;
        else if (f > 2) ntype = this.randomNodeType();
        floorNodes.push(new MapNode(ntype, f, i, i));
      }
      this.floors.push(floorNodes);
    }
    this.connectFloors();
    for (const node of this.floors[0]) node.available = true;
  }

  randomNodeType(): string {
    const roll = Math.random();
    if (roll < 0.45) return NODE_COMBAT;
    if (roll < 0.57) return NODE_ELITE;
    if (roll < 0.67) return NODE_SHOP;
    if (roll < 0.75) return NODE_TREASURE;
    if (roll < 0.92) return NODE_EVENT;
    return NODE_REST;
  }

  connectFloors() {
    for (let f = 0; f < this.floors.length - 1; f++) {
      for (const node of this.floors[f]) {
        const next = this.floors[f + 1];
        const target = next[Math.floor(Math.random() * next.length)];
        node.connections.push(target);
      }
    }
  }

  selectNode(node: MapNode): boolean {
    if (!node.available || node.completed) return false;
    if (this.currentNode) {
      const linked = this.currentNode.connections.includes(node);
      if (this.currentNode.floor + 1 !== node.floor || !linked) return false;
    }
    for (const floor of this.floors) {
      for (const n of floor) n.available = false;
    }
    node.visited = true;
    this.currentNode = node;
    for (const next of node.connections) next.available = true;
    return true;
  }

  completeCurrentNode() {
    if (this.currentNode) this.currentNode.completed = true;
  }

  getFloorProgress(): [number, number] {
    const floor = this.currentNode?.floor ?? 0;
    return [floor, GameMap.FLOORS];
  }
}
