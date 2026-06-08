func TestGetUser(t *testing.T) {
    db, mock, err := sqlmock.New()
    require.NoError(t, err)
    defer db.Close()

    mock.ExpectQuery("SELECT (.+) FROM users WHERE id = \\$1").
        WithArgs(42).
        WillReturnRows(sqlmock.NewRows([]string{"id", "name"}).
            AddRow(42, "Timur"))

    repo := NewUserRepository(db)
    user, err := repo.GetUser(context.Background(), 42)
    require.NoError(t, err)
    assert.Equal(t, "Timur", user.Name)

    assert.NoError(t, mock.ExpectationsWereMet())
}
