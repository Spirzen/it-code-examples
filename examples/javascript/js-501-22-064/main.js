const date = new Date(2024, 0, 15, 14, 30, 45);

// Различные форматы для русской локали
console.log(new Intl.DateTimeFormat("ru-RU").format(date));
// "15.01.2024"

console.log(new Intl.DateTimeFormat("ru-RU", { dateStyle: "full" }).format(date));
// "понедельник, 15 января 2024 г."

console.log(new Intl.DateTimeFormat("ru-RU", { 
    dateStyle: "long", 
    timeStyle: "short" 
}).format(date));
// "15 января 2024 г., 14:30"

console.log(new Intl.DateTimeFormat("ru-RU", {
    year: "numeric",
    month: "long",
    day: "numeric",
    weekday: "long",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    timeZoneName: "short"
}).format(date));
// "понедельник, 15 января 2024 г., 14:30:45, MSK"
