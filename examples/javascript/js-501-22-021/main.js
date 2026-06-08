class Parent {
    greet() {
        return "Привет от родителя";
    }
}

class Child extends Parent {
    greet() {
        return super.greet() + " и от ребёнка";
    }
}

const child = new Child();
console.log(child.greet()); // "Привет от родителя и от ребёнка"
