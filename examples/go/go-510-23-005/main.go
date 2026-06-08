type mockEmailClient struct {
    called bool
}

func (m *mockEmailClient) Send(ctx context.Context, to, msg string) error {
    m.called = true
    return nil
}

// В тесте:
client := &mockEmailClient{}
svc := NewUserService(repo, client)
_ = svc.WelcomeUser(ctx, "id123")
if !client.called {
    t.Error("email not sent")
}
