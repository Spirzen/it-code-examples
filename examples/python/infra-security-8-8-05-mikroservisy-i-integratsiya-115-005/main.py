
import grpc
import user_pb2
import user_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = user_pb2_grpc.UserServiceStub(channel)
    
    # Получение пользователя
    response = stub.GetUser(user_pb2.UserRequest(user_id=1))
    print(f"User: {response.name}, Email: {response.email}")
    
    # Создание пользователя
    new_user = stub.CreateUser(user_pb2.UserResponse(
        name="Тимур",
        email="timur@example.com",
        is_active=True
    ))
    print(f"Created user ID: {new_user.user_id}")

if __name__ == '__main__':
    run()
