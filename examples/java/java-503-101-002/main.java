// Хорошо
if (condition) {
    doSomething();
} else {
    doSomethingElse();
}

for (int i = 0; i < 10; i++) {
    process(i);
}

// Плохо
if (condition)
    doSomething();

if (condition) doSomething();

if (condition) {
    doSomething(); } // закрывающая скобка не на новой строке
