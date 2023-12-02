import grpc
import reddit_pb2
import reddit_pb2_grpc

posts = {
    "0011": reddit_pb2.Post(
        id="0011",
        title="Dummy Post Title 0011",
        content="Dummy Post Content",
        user_id="user1",
        score=1000,
        state=reddit_pb2.Post.PostState.NORMAL,
        image_url="./dummy.jpg",
        publication_date="12/02/2023, 14:01:56",
    )
}
comments = {}

# populate posts and comments
for i in range(100):
    posts[str(i)] = reddit_pb2.Post(
        id=str(i),
        title=f"Dummy Post Title {i}",
        content="Dummy Post Content",
        image_url="./dummy.jpg",
        user_id=f"user{i}",
        score=i,
        publication_date="12/02/2023, 14:01:56",
    )
    # for testing purpose, give post0 100 comments
    comments[str(i)] = reddit_pb2.Comment(
        id=str(i),
        user_id=f"user{i}",
        parent_post_id="0",
        content=f"Dummy Comment Content {i}",
        score=100 - i,
        state=reddit_pb2.Comment.CommentState.NORMAL,
        publication_date="12/02/2023, 14:01:57",
    )

# give first 50 comments comments subcomment
for i in range(100, 150):
    comments[str(i)] = reddit_pb2.Comment(
        id=str(i),
        user_id=f"user{i}",
        parent_comment_id=str(i - 100),
        content=f"Dummy Comment Content {i}",
        score=100 - i,
        state=reddit_pb2.Comment.CommentState.NORMAL,
        publication_date="12/02/2023, 14:01:58",
    )
