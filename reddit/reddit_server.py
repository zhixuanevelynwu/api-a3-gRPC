import grpc
from concurrent import futures
import reddit_pb2
import reddit_pb2_grpc
import uuid
from datetime import datetime
import threading

# dummy data
posts = {}
comments = {}


class RedditServicer(reddit_pb2_grpc.RedditService):
    posts_lock = threading.Lock()

    def CreatePost(self, request, context):
        # create a unique post id
        post_id = str(uuid.uuid4())

        # get data from request
        title = request.title
        content = request.content
        user_id = request.user_id
        image_url = request.image_url
        video_url = request.video_url

        # must haves
        if title == "" or content == "" or (image_url != "" and video_url != ""):
            context.set_details("Invalid post!")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return reddit_pb2.Post()

        now = datetime.now()
        publication_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        # create post object
        new_post = reddit_pb2.Post(
            id=post_id,
            title=title,
            content=content,
            user_id=user_id,
            score=0,  # initial score
            state=reddit_pb2.Post.PostState.NORMAL,  # initial state
            publication_date=publication_date,  # current time
        )

        if image_url:
            new_post.image_url = image_url
        elif video_url:
            new_post.video_url = video_url

        posts[post_id] = new_post
        return new_post

    def UpvotePost(self, request, context):
        post_id = request.id
        with self.posts_lock:
            post = posts.get(post_id, None)
            if post:
                post.score += 1
                return post
            else:
                context.set_details("Post not found!")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return reddit_pb2.Post()

    def DownvotePost(self, request, context):
        post_id = request.id
        with self.posts_lock:
            post = posts.get(post_id, None)
            if post:
                post.score -= 1
                return post
            else:
                context.set_details("Post not found!")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return reddit_pb2.Post()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reddit_pb2_grpc.add_RedditServiceServicer_to_server(RedditServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
