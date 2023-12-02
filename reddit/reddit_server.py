import grpc
from concurrent import futures
import reddit_pb2
import reddit_pb2_grpc
import uuid
from datetime import datetime
import threading
from db import posts, comments


class RedditServicer(reddit_pb2_grpc.RedditService):
    posts_lock = threading.Lock()

    # create a new post
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

    # upvate an existing post
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

    # downvote an existing post
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

    # retrieve an existing post
    def RetrievePostContent(self, request, context):
        post_id = request.id
        post = posts.get(post_id, None)

        # post must exist
        if post:
            return post
        else:
            context.set_details("Post not found!")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return reddit_pb2.Post()

    # create a new comment
    def CreateComment(self, request, context):
        # create a unique comment id
        comment_id = str(uuid.uuid4())

        # get data from request
        user_id = request.user_id
        content = request.content
        parent_post_id = request.parent_post_id
        parent_comment_id = request.parent_comment_id

        # must haves
        if content == "" or user_id == "":
            context.set_details("Invalid comment!")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return reddit_pb2.Comment()

        # must be under a post or a comment
        if parent_post_id == "" and parent_comment_id == "":
            context.set_details("Invalid comment!")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return reddit_pb2.Comment()

        # the parent must already exist in our database
        parent = None
        if parent_post_id != "":
            parent = posts.get(parent_post_id, None)
        else:
            parent = comments.get(parent_comment_id, None)
        if not parent:
            context.set_details("Parent not found!")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return reddit_pb2.Comment()

        # all passed, get now time
        now = datetime.now()
        publication_date = now.strftime("%m/%d/%Y, %H:%M:%S")

        # create comment object
        new_comment = reddit_pb2.Comment(
            id=comment_id,
            user_id=user_id,
            content=content,
            score=0,  # initial score
            state=reddit_pb2.Comment.CommentState.NORMAL,  # initial state
            publication_date=publication_date,  # current time
        )

        # set parent id
        if parent_post_id != "":
            new_comment.parent_post_id = parent_post_id
        else:
            new_comment.parent_comment_id = parent_comment_id

        comments[comment_id] = new_comment
        return new_comment

    """
    rpc RetrieveTopComments(RetrieveTopCommentsRequest) returns (RetrieveTopCommentsResponse);
    """
    # retrieve


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reddit_pb2_grpc.add_RedditServiceServicer_to_server(RedditServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
