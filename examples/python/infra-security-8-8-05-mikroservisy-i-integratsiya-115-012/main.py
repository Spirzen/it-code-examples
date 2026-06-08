
import strawberry

from typing import List, Optional
from datetime import datetime

@strawberry.type
class User:
    id: int
    name: str
    email: str
    is_active: bool
    created_at: str
    
    @strawberry.field
    def posts(self) -> List["Post"]:
        return [post for post in posts if post.author_id == self.id]

@strawberry.type
class Post:
    id: int
    title: str
    content: str
    author_id: int
    published_at: str
    
    @strawberry.field
    def author(self) -> User:
        return next(user for user in users if user.id == self.author_id)

# Хранилище данных
users: List[User] = []
posts: List[Post] = []

@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> Optional[User]:
        return next((u for u in users if u.id == id), None)
    
    @strawberry.field
    def users(self, page: int = 1, page_size: int = 10) -> List[User]:
        start = (page - 1) * page_size
        return users[start:start + page_size]
    
    @strawberry.field
    def post(self, id: int) -> Optional[Post]:
        return next((p for p in posts if p.id == id), None)
    
    @strawberry.field
    def posts(self, page: int = 1, page_size: int = 10) -> List[Post]:
        start = (page - 1) * page_size
        return posts[start:start + page_size]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str, email: str, is_active: bool = True) -> User:
        user = User(
            id=len(users) + 1,
            name=name,
            email=email,
            is_active=is_active,
            created_at=datetime.utcnow().isoformat()
        )
        users.append(user)
        return user
    
    @strawberry.mutation
    def update_user(
        self, 
        id: int, 
        name: Optional[str] = None,
        email: Optional[str] = None,
        is_active: Optional[bool] = None
    ) -> User:
        user = next((u for u in users if u.id == id), None)
        if not user:
            raise Exception("User not found")
        
        if name: user.name = name
        if email: user.email = email
        if is_active is not None: user.is_active = is_active
        
        return user
    
    @strawberry.mutation
    def delete_user(self, id: int) -> bool:
        global users
        initial_count = len(users)
        users = [u for u in users if u.id != id]
        return len(users) < initial_count
    
    @strawberry.mutation
    def create_post(self, title: str, content: str, author_id: int) -> Post:
        author = next((u for u in users if u.id == author_id), None)
        if not author:
            raise Exception("Author not found")
        
        post = Post(
            id=len(posts) + 1,
            title=title,
            content=content,
            author_id=author_id,
            published_at=datetime.utcnow().isoformat()
        )
        posts.append(post)
        return post

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def user_created(self) -> User:
        # Реализация через asyncio.Queue или Redis Pub/Sub
        pass

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)
