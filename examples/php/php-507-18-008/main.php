trait A {
    public function greet() { return "Привет от A"; }
}

trait B {
    public function greet() { return "Привет от B"; }
}

class C {
    use A, B {
        A::greet insteadof B; // использовать реализацию из A
        B::greet as greetFromB; // оставить копию под новым именем
    }
}
