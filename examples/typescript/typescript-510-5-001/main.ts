export type Todo = {
  id: number;
  title: string;
  done: boolean;
};

const todos: Todo[] = [];

export function addTodo(title: string): Todo {
  const todo: Todo = {
    id: Date.now(),
    title: title.trim(),
    done: false,
  };
  if (!todo.title) throw new Error("title required");
  todos.push(todo);
  return todo;
}

export function completeTodo(id: number): Result<"ok" | "not-found"> {
  const todo = todos.find((t) => t.id === id);
  if (!todo) return { ok: false, error: "not-found" };
  todo.done = true;
  return { ok: true, value: "ok" };
}

type Result<T, E = string> =
  | { ok: true; value: T }
  | { ok: false; error: E };

export function listTodos(): readonly Todo[] {
  return todos;
}
