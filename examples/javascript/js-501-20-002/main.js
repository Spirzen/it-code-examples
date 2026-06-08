const uniqueNumbers = new Set([1, 2, 3, 4, 5]);

for (let num of uniqueNumbers) {
    console.log(num);
}

const phoneBook = new Map([
    ["Джон", "555-1234"],
    ["Мария", "555-5678"]
]);

for (let [name, phone] of phoneBook) {
    console.log(`${name}: ${phone}`);
}
