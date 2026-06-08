class User {
    public $name;

    public function __construct($name) {
        $this->name = $name;
    }

    public function sayHello() {
        return "Привет, " . $this->name;
    }
}

$user = new User("Петр");
echo $user->sayHello();
