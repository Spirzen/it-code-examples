type ApiResult =
  | { status: "ok"; data: string }
  | { status: "error"; code: number };

function handle(result: ApiResult): string {
  switch (result.status) {
    case "ok":
      return result.data;
    case "error":
      return `Ошибка ${result.code}`;
    default: {
      const _exhaustive: never = result;
      return _exhaustive;
    }
  }
}
