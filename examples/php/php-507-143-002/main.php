class Post extends Model
{
    public function comments()
    {
        return $this->hasMany(Comment::class);
    }
}

$posts = Post::with('comments')->get();
foreach ($posts as $post) {
    foreach ($post->comments as $comment) {
        echo $comment->text;
    }
}
