import grpc
import reddit_pb2
import reddit_pb2_grpc

posts = {
    "0011": reddit_pb2.Post(
        id="0011",
        title="Dummy Post Title",
        content="Dummy Post Content",
        image_url="./dummy.jpg",
        user_id="user1",
        publication_date="12/02/2023, 14:01:56",
    )
}
comments = {}
