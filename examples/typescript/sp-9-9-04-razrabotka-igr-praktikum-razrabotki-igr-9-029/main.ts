import type { SessionStats } from './types';

const KEY = 'tower_shadows_stats';

const defaultStats = (): SessionStats => ({
  totalRuns: 0,
  totalWins: 0,
  bestFloor: 0,
  totalKills: 0,
  dailyBestFloor: 0,
  leaderboard: [],
});

export function loadSessionStats(): SessionStats {
  try {
    const raw = localStorage.getItem(KEY);
    return raw ? { ...defaultStats(), ...JSON.parse(raw) } : defaultStats();
  } catch {
    return defaultStats();
  }
}

export function saveSessionStats(stats: SessionStats) {
  localStorage.setItem(KEY, JSON.stringify(stats));
}
