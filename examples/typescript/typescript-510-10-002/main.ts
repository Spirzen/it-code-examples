type LoadState =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: string }
  | { status: "error"; message: string };

function render(state: LoadState): string {
  switch (state.status) {
    case "idle":
      return 'Нажмите "Загрузить"';
    case "loading":
      return "Загрузка…";
    case "success":
      return state.data;
    case "error":
      return state.message;
    default: {
      const _exhaustive: never = state;
      return _exhaustive;
    }
  }
}
