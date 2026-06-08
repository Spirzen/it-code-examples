public class UserType : ObjectType<User>
{
    protected override void Configure(IObjectTypeDescriptor<User> descriptor)
    {
        descriptor.Field(u => u.Id).Type<NonNullType<IDType>>();
        descriptor.Field(u => u.Posts)
            .ResolveWith<Query>(q => q.GetPosts(default!, default!))
            .Type<ListType<NonNullType<PostType>>>();
    }
}

public class PostType : ObjectType<Post>
{
    protected override void Configure(IObjectTypeDescriptor<Post> descriptor)
    {
        descriptor.Field(p => p.Author)
            .ResolveWith<Query>(q => q.GetUser(default!))
            .Type<NonNullType<UserType>>();
    }
}
