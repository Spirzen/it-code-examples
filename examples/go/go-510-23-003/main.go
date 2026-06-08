type Generator func() ([]byte, error)

func (g Generator) Read(p []byte) (n int, err error) {
    data, err := g()
    if err != nil {
        return 0, err
    }
    n = copy(p, data)
    return n, nil
}

// Использование:
gen := Generator(func() ([]byte, error) { return []byte("Hello"), nil })
io.Copy(os.Stdout, gen)
