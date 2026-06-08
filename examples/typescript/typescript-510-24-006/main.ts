type Path<T> = T extends object
  ? {
      [K in keyof T]: K extends string ? `${K}` | `${K}.${Path<T[K]>}` : never;
    }[keyof T]
  : never;

type PathType<T, P extends Path<T>> = P extends `${infer Key}.${infer Rest}`
  ? Key extends keyof T
    ? Rest extends Path<T[Key]>
      ? PathType<T[Key], Rest>
      : never
    : never
  : P extends keyof T
    ? T[P]
    : never;

interface AppState {
  user: {
    id: string;
    preferences: {
      theme: "light" | "dark";
      lang: "en" | "es";
    };
  };
  ui: { sidebarOpen: boolean };
}

type AppStatePath = Path<AppState>;
// "user" | "ui" | "user.id" | "user.preferences" | "user.preferences.theme" | …

type Theme = PathType<AppState, "user.preferences.theme">; // "light" | "dark"
type Sidebar = PathType<AppState, "ui.sidebarOpen">; // boolean
