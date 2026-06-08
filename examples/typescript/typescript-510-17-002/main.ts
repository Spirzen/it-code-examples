function renderUserState(state: UserLoadState): string {
  switch (state.status) {
    case "idle":
      return 'Нажмите "Загрузить"';
    case "loading":
      return "Загрузка…";
    case "success":
      return state.data.name;
    case "error":
      return state.message;
    default: {
      const _exhaustive: never = state;
      return _exhaustive;
    }
  }
}
