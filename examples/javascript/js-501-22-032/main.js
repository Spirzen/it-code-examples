const EventType = {
    CLICK: Symbol("click"),
    HOVER: Symbol("hover"),
    DRAG: Symbol("drag")
};

function handleEvent(eventType) {
    switch (eventType) {
        case EventType.CLICK:
            console.log("Обработка клика");
            break;
        case EventType.HOVER:
            console.log("Обработка наведения");
            break;
        case EventType.DRAG:
            console.log("Обработка перетаскивания");
            break;
    }
}

handleEvent(EventType.CLICK); // "Обработка клика"
