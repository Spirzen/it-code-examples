const formatter = new Intl.RelativeTimeFormat("ru", { numeric: "auto" });

console.log(formatter.format(-1, "day"));    // "вчера"
console.log(formatter.format(0, "day"));     // "сегодня"
console.log(formatter.format(1, "day"));     // "завтра"
console.log(formatter.format(-2, "day"));    // "позавчера"
console.log(formatter.format(2, "day"));     // "послезавтра"

console.log(formatter.format(-1, "hour"));   // "час назад"
console.log(formatter.format(1, "hour"));    // "через час"
console.log(formatter.format(3, "hour"));    // "через 3 часа"

console.log(formatter.format(-1, "month"));  // "в прошлом месяце"
console.log(formatter.format(1, "month"));   // "в следующем месяце"
