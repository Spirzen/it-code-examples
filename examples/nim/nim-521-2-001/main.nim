import std/[options, results]

proc parsePort(s: string): Option[int] =
  try: some(parseInt(s))
  except ValueError: none(int)

proc readConfig(path: string): Result[string, string] =
  if path.len == 0:
    err("empty path")
  else:
    ok("config loaded")

echo parsePort("8080")
echo readConfig("app.cfg")
