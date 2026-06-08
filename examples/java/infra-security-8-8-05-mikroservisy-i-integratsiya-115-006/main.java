
import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import com.example.user.*;

import java.io.IOException;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class UserServiceImpl extends UserServiceGrpc.UserServiceImplBase {
    
    private final Map<Integer, UserResponse> users = new ConcurrentHashMap<>();
    
    @Override
    public void getUser(UserRequest request, StreamObserver<UserResponse> responseObserver) {
        UserResponse user = users.get(request.getUserId());
        
        if (user == null) {
            responseObserver.onError(
                io.grpc.Status.NOT_FOUND
                    .withDescription("User not found")
                    .asRuntimeException()
            );
        } else {
            responseObserver.onNext(user);
            responseObserver.onCompleted();
        }
    }
    
    @Override
    public void listUsers(UserListRequest request, StreamObserver<UserListResponse> responseObserver) {
        int skip = (request.getPage() - 1) * request.getPageSize();
        UserListResponse.Builder builder = UserListResponse.newBuilder();
        
        users.values().stream()
            .skip(skip)
            .limit(request.getPageSize())
            .forEach(builder::addUsers);
        
        builder.setTotalCount(users.size());
        responseObserver.onNext(builder.build());
        responseObserver.onCompleted();
    }
    
    @Override
    public void createUser(UserResponse request, StreamObserver<UserResponse> responseObserver) {
        int userId = users.size() + 1;
        UserResponse newUser = UserResponse.newBuilder()
            .setUserId(userId)
            .setName(request.getName())
            .setEmail(request.getEmail())
            .setIsActive(request.getIsActive())
            .build();
        
        users.put(userId, newUser);
        responseObserver.onNext(newUser);
        responseObserver.onCompleted();
    }
    
    public static void main(String[] args) throws IOException, InterruptedException {
        Server server = ServerBuilder.forPort(50051)
            .addService(new UserServiceImpl())
            .build()
            .start();
        
        System.out.println("Server started on port 50051");
        server.awaitTermination();
    }
}
