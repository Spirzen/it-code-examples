type Command =
  | { type: "create-user"; email: string; name: string }
  | { type: "ban-user"; userId: string }
  | { type: "send-email"; to: string; subject: string };

function handleCommand(command: Command): void {
  switch (command.type) {
    case "create-user":
      console.log(command.email, command.name);
      return;
    case "ban-user":
      console.log(command.userId);
      return;
    case "send-email":
      console.log(command.to, command.subject);
      return;
    default: {
      const _exhaustive: never = command;
      return _exhaustive;
    }
  }
}
