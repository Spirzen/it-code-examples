const rules = new Intl.PluralRules("ru");

console.log(rules.select(1));   // "one"
console.log(rules.select(2));   // "few"
console.log(rules.select(5));   // "many"
console.log(rules.select(11));  // "many"
console.log(rules.select(21));  // "one"
console.log(rules.select(22));  // "few"

// Практическое применение
function getMessage(count) {
    const forms = {
        one: "сообщение",
        few: "сообщения",
        many: "сообщений"
    };
    return `${count} ${forms[rules.select(count)]}`;
}

console.log(getMessage(1));   // "1 сообщение"
console.log(getMessage(2));   // "2 сообщения"
console.log(getMessage(5));   // "5 сообщений"
console.log(getMessage(21));  // "21 сообщение"
