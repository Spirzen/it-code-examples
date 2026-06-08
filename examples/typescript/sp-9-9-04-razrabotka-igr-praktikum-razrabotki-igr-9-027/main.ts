export interface ClassDef {
  id: string;
  name: string;
  hp: number;
  energy: number;
  gold: number;
  description: string;
}

export const CLASSES: ClassDef[] = [
  { id: 'warrior', name: 'Воин', hp: 85, energy: 3, gold: 99, description: 'Баланс урона и защиты.' },
  { id: 'rogue', name: 'Плут', hp: 75, energy: 3, gold: 99, description: 'Карты добора и комбо.' },
  { id: 'guardian', name: 'Страж', hp: 90, energy: 3, gold: 99, description: 'Много брони и силы.' },
];

export function getClass(id: string) {
  return CLASSES.find((c) => c.id === id) ?? CLASSES[0];
}
