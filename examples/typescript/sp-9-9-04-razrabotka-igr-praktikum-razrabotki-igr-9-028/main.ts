export class SeededRNG {
  private state: number;

  constructor(seed: number) {
    this.state = (seed >>> 0) || 1;
  }

  next(): number {
    let t = (this.state += 0x6d2b79f5);
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  }

  int(max: number) {
    return Math.floor(this.next() * max);
  }
}

let activeRng = new SeededRNG(Date.now());

export function setActiveRng(rng: SeededRNG) {
  activeRng = rng;
}

export function rngInt(max: number) {
  return activeRng.int(max);
}

export function dailySeed(): number {
  const d = new Date();
  return d.getFullYear() * 10000 + (d.getMonth() + 1) * 100 + d.getDate();
}
