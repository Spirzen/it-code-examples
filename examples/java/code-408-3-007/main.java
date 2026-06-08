class User {
    private string password; // Приватное поле

    public void setPassword(string newPassword) {
        if (newPassword.Length >= 8) {
            password = newPassword;
        } else {
            throw new Exception("Пароль слишком короткий!");
        }
    }
}
