
import std/[json, os]

type Task = object
  id: int
  title: string
  done: bool

proc load(path: string): seq[Task] =
  if not fileExists(path):
    return @[]
  let data = parseJson(readFile(path))
  if data.kind != JArray:
    raise newException(ValueError, "Ожидался JSON-массив")
  for item in data:
    result.add Task(
      id: item["id"].getInt,
      title: item["title"].getStr,
      done: item["done"].getBool
    )

proc save(path: string, tasks: seq[Task]) =
  var arr = newJArray()
  for t in tasks:
    arr.add %*{
      "id": t.id,
      "title": t.title,
      "done": t.done
    }
  writeFile(path, $arr)

when isMainModule:
  const path = "tasks.json"
  var tasks = load(path)
  tasks.add Task(id: tasks.len + 1, title: "Изучить Nim", done: false)
  save(path, tasks)
  echo "Записано задач: ", tasks.len
