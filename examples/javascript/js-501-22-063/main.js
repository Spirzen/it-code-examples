const names = ["Иван", "Анна", "Петр", "Елена"];

// Сортировка без учёта локали
console.log(names.sort());
// ["Анна", "Елена", "Иван", "Петр"]

// Сортировка с учётом русской локали
const collator = new Intl.Collator("ru");
console.log(names.sort((a, b) => collator.compare(a, b)));
// ["Анна", "Елена", "Иван", "Петр"]

// Сортировка с игнорированием регистра
const caseInsensitive = new Intl.Collator("ru", { sensitivity: "base" });
console.log(caseInsensitive.compare("Тест", "тест")); // 0 (равны)
