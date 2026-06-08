// Абстракция в доменном пакете
package user

type Repository interface {
    FindByID(id string) (*User, error)
    Save(u *User) error
}

type Service struct {
    repo Repository
}

func NewService(repo Repository) *Service {
    return &Service{repo: repo}
}
