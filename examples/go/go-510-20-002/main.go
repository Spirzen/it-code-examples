// ent/schema/user.go
func (User) Fields() []ent.Field {
    return []ent.Field{
        field.String("name").
            Default("unknown"),
        field.String("email").
            Unique(),
    }
}

func (User) Edges() []ent.Edge {
    return []ent.Edge{
        edge.To("posts", Post.Type),
    }
}
