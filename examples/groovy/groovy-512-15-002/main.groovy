class Person {
    private String name

    String getName() {
        return name?.toUpperCase()
    }

    void setName(String value) {
        if (value && value.length() > 2) {
            this.name = value
        } else {
            throw new IllegalArgumentException("Name must be at least 3 characters long")
        }
    }
}
