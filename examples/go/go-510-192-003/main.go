func TestParseAge(t *testing.T) {
    tests := []struct {
        name    string
        in      string
        want    int
        wantErr bool
    }{
        {"ok", "21", 21, false},
        {"bad_format", "x21", 0, true},
        {"negative", "-1", 0, true},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got, err := parseAge(tt.in)
            if (err != nil) != tt.wantErr {
                t.Fatalf("err presence = %v, wantErr %v", err != nil, tt.wantErr)
            }
            if got != tt.want {
                t.Errorf("got %d, want %d", got, tt.want)
            }
        })
    }
}
