interface Logger {
  log(message: string): void;
}

class ConsoleLogger implements Logger {
  log(message: string): void {
    console.log(message);
  }
}

class JsonLogger implements Logger {
  log(message: string): void {
    console.log(JSON.stringify({ message }));
  }
}

type LoggerKind = "console" | "json";

function createLogger(kind: LoggerKind): Logger {
  switch (kind) {
    case "console":
      return new ConsoleLogger();
    case "json":
      return new JsonLogger();
  }
}
