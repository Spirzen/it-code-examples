type InputEvent = {
  type: "input";
  value: string;
};

type ClickEvent = {
  type: "click";
  x: number;
  y: number;
};

type AppEvent = InputEvent | ClickEvent;

function handleEvent(event: AppEvent): void {
  switch (event.type) {
    case "input":
      console.log(event.value);
      return;
    case "click":
      console.log(event.x, event.y);
      return;
  }
}
