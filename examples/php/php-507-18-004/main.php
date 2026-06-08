   class Animal {
       public function makeSound(): string {
           return "…";
       }
   }

   class Dog extends Animal {
       public function makeSound(): string {
           return "Гав";
       }
   }

   class Cat extends Animal {
       public function makeSound(): string {
           return "Мяу";
       }
   }

   function announce(Animal $animal): void {
       echo $animal->makeSound();
   }

   announce(new Dog()); // → "Гав"
   announce(new Cat()); // → "Мяу"
