
import graphql.schema.GraphQLObjectType;
import graphql.schema.GraphQLSchema;
import graphql.schema.idl.RuntimeWiring;
import graphql.schema.idl.SchemaGenerator;
import graphql.schema.idl.SchemaParser;
import graphql.schema.idl.TypeDefinitionRegistry;

import java.io.InputStream;

public class GraphQLSchemaProvider {
    
    public GraphQLSchema createSchema() {
        SchemaParser parser = new SchemaParser();
        TypeDefinitionRegistry typeRegistry = parser.parse(
            this.getClass().getResourceAsStream("/schema.graphqls")
        );
        
        RuntimeWiring wiring = RuntimeWiring.newRuntimeWiring()
            .type("Query", typeWiring -> typeWiring
                .dataFetcher("user", new UserDataFetcher())
                .dataFetcher("users", new UsersDataFetcher())
                .dataFetcher("post", new PostDataFetcher())
                .dataFetcher("posts", new PostsDataFetcher())
            )
            .type("Mutation", typeWiring -> typeWiring
                .dataFetcher("createUser", new CreateUserMutation())
                .dataFetcher("updateUser", new UpdateUserMutation())
                .dataFetcher("deleteUser", new DeleteUserMutation())
                .dataFetcher("createPost", new CreatePostMutation())
            )
            .type("User", typeWiring -> typeWiring
                .dataFetcher("posts", new UserPostsDataFetcher())
            )
            .type("Post", typeWiring -> typeWiring
                .dataFetcher("author", new PostAuthorDataFetcher())
            )
            .build();
        
        SchemaGenerator generator = new SchemaGenerator();
        return generator.makeExecutableSchema(typeRegistry, wiring);
    }
}
