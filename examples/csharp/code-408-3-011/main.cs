class ImmutableUser {
    public string Name { get; } // Только для чтения
    public int Age { get; }

    public ImmutableUser(string name, int age) {
        Name = name;
        Age = age;
    }
}
