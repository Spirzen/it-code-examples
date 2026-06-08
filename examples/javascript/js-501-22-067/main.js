const formatter = new Intl.ListFormat("ru", { 
    style: "long", 
    type: "conjunction" 
});

console.log(formatter.format(["яблоки"]));              // "яблоки"
console.log(formatter.format(["яблоки", "груши"]));     // "яблоки и груши"
console.log(formatter.format(["яблоки", "груши", "апельсины"])); 
// "яблоки, груши и апельсины"

// Другие типы
const disjunction = new Intl.ListFormat("ru", { type: "disjunction" });
console.log(disjunction.format(["да", "нет"])); // "да или нет"

const unit = new Intl.ListFormat("ru", { type: "unit" });
console.log(unit.format(["метр", "килограмм"])); // "метр, килограмм"
