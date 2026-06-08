
import grpc

from concurrent import futures

import user_pb2
import user_pb2_grpc

class UserServiceImpl(user_pb2_grpc.UserServiceServicer):
    def __init__(self):
        self.users = {}
    
    def GetUser(self, request, context):
        user = self.users.get(request.user_id)
        if not user:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User not found')
            return user_pb2.UserResponse()
        return user
    
    def ListUsers(self, request, context):
        skip = (request.page - 1) * request.page_size
        users_list = list(self.users.values())[skip:skip + request.page_size]
        
        return user_pb2.UserListResponse(
            users=users_list,
            total_count=len(self.users)
        )
    
    def CreateUser(self, request, context):
        user_id = len(self.users) + 1
        new_user = user_pb2.UserResponse(
            user_id=user_id,
            name=request.name,
            email=request.email,
            is_active=request.is_active
        )
        self.users[user_id] = new_user
        return new_user

# Запуск сервера
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserServiceImpl(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
