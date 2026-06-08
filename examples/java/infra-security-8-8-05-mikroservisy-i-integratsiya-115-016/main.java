
import graphql.GraphQL;
import graphql.schema.GraphQLSchema;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class GraphQLConfig {
    
    @Bean
    public GraphQL graphQL(GraphQLSchemaProvider schemaProvider) {
        GraphQLSchema schema = schemaProvider.createSchema();
        return GraphQL.newGraphQL(schema).build();
    }
}

@RestController
@RequestMapping("/graphql")
public class GraphQLController {
    
    @Autowired
    private GraphQL graphQL;
    
    @PostMapping(produces = "application/json")
    public ResponseEntity<Object> graphql(@RequestBody String query) {
        ExecutionInput executionInput = ExecutionInput.newExecutionInput()
            .query(query)
            .build();
        
        ExecutionResult executionResult = graphQL.execute(executionInput);
        return ResponseEntity.ok(executionResult.toSpecification());
    }
}
