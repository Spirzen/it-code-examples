func TestBuildGreeting(t *testing.T) {
    cases := []struct {
        in   string
        want string
    }{
        {"Alice", "Hello, Alice!"},
        {"Bob", "Hello, Bob!"},
    }

    for _, c := range cases {
        if got := buildGreeting(c.in); got != c.want {
            t.Fatalf("got %q, want %q", got, c.want)
        }
    }
}
