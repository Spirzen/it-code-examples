type UserRepo struct {
    db *sql.DB
}

func NewUserRepo(db *sql.DB) *UserRepo {
    return &UserRepo{db: db}
}

func (r *UserRepo) GetByID(ctx context.Context, id int64) (User, error) {
    var u User
    err := r.db.QueryRowContext(ctx,
`SELECT id, name, email FROM users WHERE id = $1`, id,
    ).Scan(&u.ID, &u.Name, &u.Email)
    if err != nil {
        return User{}, fmt.Errorf("get user by id %d: %w", id, err)
    }
    return u, nil
}
