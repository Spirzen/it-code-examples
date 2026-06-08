type Option<T> =
  | { tag: 'some'; value: T }
  | { tag: 'none' };

type Result<T, E = string> =
  | { ok: true; value: T }
  | { ok: false; error: E };

function findUser(id: string): Option<User> {
  const u = db.get(id);
  return u ? { tag: 'some', value: u } : { tag: 'none' };
}

function loadConfig(path: string): Result<Config, 'not-found' | 'invalid-json'> {
  // ...
}
