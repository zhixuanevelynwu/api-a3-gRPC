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
    comments_lock = threading.Lock()

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

    # upvate an existing comment
    def UpvoteComment(self, request, context):
        comment_id = request.id
        with self.comments_lock:
            comment = comments.get(comment_id, None)
            if comment:
                comment.score += 1
                return comment
            else:
                context.set_details("Comment not found!")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return reddit_pb2.Comment()

    # downvote an existing comment
    def DownvoteComment(self, request, context):
        comment_id = request.id
        with self.comments_lock:
            comment = comments.get(comment_id, None)
            if comment:
                comment.score -= 1
                return comment
            else:
                context.set_details("Comment not found!")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return reddit_pb2.Comment()

    # Retrieving a list of N most upvoted comments under a post, where N is a parameter to the call
    def RetrieveTopNComments(self, request, context):
        # get data from request
        post_id = request.id
        N = request.N
        post = posts.get(post_id, None)

        # must have post
        if not post:
            context.set_details("Post not found!")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return reddit_pb2.RetrieveTopNCommentsResponse()

        # get all comments under this post
        all_comments_under_post = []
        for comment in comments.values():
            if comment.parent_post_id == post_id:
                all_comments_under_post.append(comment)

        # sort comments by score
        all_comments_under_post.sort(key=lambda x: x.score, reverse=True)

        # get top N comments, if there are less than N comments, return all
        N = min(N, len(all_comments_under_post))
        top_N_comments_with_has_replies = []
        # indicate whether there are replies under those comments
        for comment in all_comments_under_post[:N]:
            for subcomment in comments.values():
                has_replies = False
                if subcomment.parent_comment_id == comment.id:
                    has_replies = True
                    break
            top_N_comments_with_has_replies.append(
                reddit_pb2.CommentWithHasReplies(
                    comment=comment, has_replies=has_replies
                )
            )
        return reddit_pb2.RetrieveTopNCommentsResponse(
            comments_with_has_replies=top_N_comments_with_has_replies
        )

    def ExpandCommentBranch(self, request, context):
        parent_comment_id = request.id
        N = request.N

        # find the parent comment, must exist
        parent_comment = comments.get(parent_comment_id, None)
        if not parent_comment:
            context.set_details("Parent comment not found!")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return reddit_pb2.ExpandCommentBranchResponse()

        # find all (direct) replies to the parent comment
        replies = [
            c for c in comments.values() if c.parent_comment_id == parent_comment_id
        ]

        # sort them in desc order by score
        replies.sort(key=lambda c: c.score, reverse=True)
        N = min(N, len(replies))
        top_N_replies = []

        # For each top reply, find and sort its replies
        for reply in replies[:N]:
            sub_replies = [
                c for c in comments.values() if c.parent_comment_id == reply.id
            ]
            sub_replies.sort(key=lambda c: c.score, reverse=True)
            top_N_sub_replies = sub_replies[:N]
            top_N_replies.append(
                reddit_pb2.CommentWithReplies(comment=reply, replies=top_N_sub_replies)
            )

        return reddit_pb2.ExpandCommentBranchResponse(
            comments_with_replies=top_N_replies
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reddit_pb2_grpc.add_RedditServiceServicer_to_server(RedditServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started at [::]:50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
