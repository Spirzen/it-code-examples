
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import com.example.user.*;

public class UserClient {
    public static void main(String[] args) {
        ManagedChannel channel = ManagedChannelBuilder
            .forAddress("localhost", 50051)
            .usePlaintext()
            .build();
        
        UserServiceGrpc.UserServiceBlockingStub stub = 
            UserServiceGrpc.newBlockingStub(channel);
        
        // Получение пользователя
        UserResponse user = stub.getUser(
            UserRequest.newBuilder().setUserId(1).build()
        );
        System.out.println("User: " + user.getName() + ", Email: " + user.getEmail());
        
        // Создание пользователя
        UserResponse newUser = stub.createUser(
            UserResponse.newBuilder()
                .setName("Тимур")
                .setEmail("timur@example.com")
                .setIsActive(true)
                .build()
        );
        System.out.println("Created user ID: " + newUser.getUserId());
        
        channel.shutdown();
    }
}
