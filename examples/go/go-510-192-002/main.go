type UserStore interface {
    Save(name string) error
}

type fakeStore struct {
    saved []string
}

func (f *fakeStore) Save(name string) error {
    f.saved = append(f.saved, name)
    return nil
}

func TestService_Register(t *testing.T) {
    store := &fakeStore{}
    svc := NewService(store)
    require.NoError(t, svc.Register("Ann"))
    assert.Equal(t, []string{"Ann"}, store.saved)
}
