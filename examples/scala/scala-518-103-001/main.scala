// build.sbt: libraryDependencies += "com.lihaoyi" %% "upickle" % "4.0.2"

import upickle.default.*

case class Task(id: Long, title: String, done: Boolean = false)

def load(path: os.Path): Seq[Task] =
  if (!os.exists(path)) Nil else read[Seq[Task]](os.read(path))

def save(path: os.Path, tasks: Seq[Task]): Unit =
  os.write(path, write(tasks, indent = 2))

@main def runTracker(): Unit = {
  val path = os.pwd / "tasks.json"
  val tasks = load(path) :+ Task(System.currentTimeMillis(), "Новая задача")
  save(path, tasks)
  println(read[Seq[Task]](os.read(path)))
}
