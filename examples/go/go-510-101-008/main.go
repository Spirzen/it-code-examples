// User представляет зарегистрированного пользователя системы.
type User struct {
    ID        string
    Email     string
    Name      string
    CreatedAt time.Time
    Active    bool
}

// IsPremium проверяет, имеет ли пользователь премиум-статус.
func (u *User) IsPremium() bool {
    return strings.HasSuffix(u.Email, "@premium.example.com")
}

// Validate проверяет корректность данных пользователя.
func (u *User) Validate() error {
    if u.Email == "" {
        return errors.New("email is required")
    }
    if !isValidEmail(u.Email) {
        return fmt.Errorf("invalid email format: %s", u.Email)
    }
    if u.Name == "" {
        return errors.New("name is required")
    }
    return nil
}
