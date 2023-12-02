import grpc
import reddit_pb2
import reddit_pb2_grpc


class RedditClient:
    def __init__(self, host="localhost", port=50051):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = reddit_pb2_grpc.RedditServiceStub(self.channel)

    def create_post(self, title, content, user_id, image_url="", video_url=""):
        post = reddit_pb2.CreatePostRequest(
            title=title,
            content=content,
            user_id=user_id,
            image_url=image_url,
            video_url=video_url,
        )
        return self.stub.CreatePost(post)

    def upvote_post(self, post_id):
        return self.stub.UpvotePost(reddit_pb2.VotePostRequest(id=post_id))

    def downvote_post(self, post_id):
        return self.stub.DownvotePost(reddit_pb2.VotePostRequest(id=post_id))

    def retrieve_post_content(self, post_id):
        return self.stub.RetrievePostContent(reddit_pb2.RetrievePostRequest(id=post_id))

    def create_comment(self, user_id, content, parent_post_id="", parent_comment_id=""):
        comment = reddit_pb2.CreateCommentRequest(
            user_id=user_id,
            content=content,
            parent_post_id=parent_post_id,
            parent_comment_id=parent_comment_id,
        )
        return self.stub.CreateComment(comment)

    def upvote_comment(self, comment_id):
        return self.stub.UpvoteComment(reddit_pb2.VoteCommentRequest(id=comment_id))

    def downvote_comment(self, comment_id):
        return self.stub.DownvoteComment(reddit_pb2.VoteCommentRequest(id=comment_id))

    def retrieve_top_n_comments(self, post_id, N):
        request = reddit_pb2.RetrieveTopNCommentsRequest(id=post_id, N=N)
        return self.stub.RetrieveTopNComments(request)

    def expand_comment_branch(self, comment_id, N):
        request = reddit_pb2.ExpandCommentBranchRequest(id=comment_id, N=N)
        return self.stub.ExpandCommentBranch(request)

    def close(self):
        self.channel.close()


def main():
    client = RedditClient(host="localhost", port=50051)

    response = client.create_post(
        title="Hello!", content="This is my post :D", user_id="user123"
    )
    print(
        f"Post created for {response.user_id}: \n{response.title} {response.content} [{response.publication_date}]"
    )

    client.close()


if __name__ == "__main__":
    main()
