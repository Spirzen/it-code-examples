
import graphql.schema.DataFetcher;
import graphql.schema.DataFetchingEnvironment;

import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.stream.Collectors;

public class UserDataFetcher implements DataFetcher<User> {
    
    private final Map<Integer, User> users = new ConcurrentHashMap<>();
    
    @Override
    public User get(DataFetchingEnvironment environment) {
        Integer id = environment.getArgument("id");
        return users.get(id);
    }
}

public class UsersDataFetcher implements DataFetcher<List<User>> {
    
    private final Map<Integer, User> users = new ConcurrentHashMap<>();
    
    @Override
    public List<User> get(DataFetchingEnvironment environment) {
        Integer page = environment.getArgument("page");
        Integer pageSize = environment.getArgument("pageSize");
        
        int skip = (page - 1) * pageSize;
        return users.values().stream()
            .skip(skip)
            .limit(pageSize)
            .collect(Collectors.toList());
    }
}
