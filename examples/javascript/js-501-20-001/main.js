const car = {
    brand: "Toyota",
    model: "Camry",
    year: 2020,
    color: "blue"
};

for (let property in car) {
    console.log(`${property}: ${car[property]}`);
}
// brand: Toyota
// model: Camry
// year: 2020
// color: blue
