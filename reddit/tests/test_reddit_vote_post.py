import sys
import os
import unittest
from unittest.mock import patch
import grpc

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import reddit_pb2
import reddit_server

mock_post_id = "1010"


class TestVotePost(unittest.TestCase):
    def setUp(self):
        self.servicer = reddit_server.RedditServicer()

    # happy path
    def test_upvote_post(self):
        # create mock request
        request = reddit_pb2.Post(id=mock_post_id)

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        # get old upvote count
        old_upvote_count = reddit_server.posts[mock_post_id].score

        # upvote the post
        self.servicer.UpvotePost(request, mock_context)

        # check if the score is incremented
        self.assertEqual(reddit_server.posts[mock_post_id].score, old_upvote_count + 1)

    # upvote non-existent post
    def test_upvote_nonexistent_post(self):
        # create mock request
        request = reddit_pb2.Post(id="nonexistent")

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        self.servicer.UpvotePost(request, mock_context)
        mock_context.set_details.assert_called_with("Post not found!")
        mock_context.set_code.assert_called_with(grpc.StatusCode.NOT_FOUND)

    # happy path
    def test_downvote_post(self):
        # create mock request
        request = reddit_pb2.Post(id=mock_post_id)

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        # get old upvote count
        old_upvote_count = reddit_server.posts[mock_post_id].score

        # downvote the post
        self.servicer.DownvotePost(request, mock_context)

        # check if the score is incremented
        self.assertEqual(reddit_server.posts[mock_post_id].score, old_upvote_count - 1)

    # downvote non-existent post
    def test_downvote_nonexistent_post(self):
        # create mock request
        request = reddit_pb2.Post(id="nonexistent")

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        self.servicer.DownvotePost(request, mock_context)

        mock_context.set_details.assert_called_with("Post not found!")
        mock_context.set_code.assert_called_with(grpc.StatusCode.NOT_FOUND)


if __name__ == "__main__":
    unittest.main()
