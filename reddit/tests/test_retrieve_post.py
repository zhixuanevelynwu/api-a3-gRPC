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
import db

mock_post_id = "1010"


class TestRetrievePostContent(unittest.TestCase):
    def setUp(self):
        self.servicer = reddit_server.RedditServicer()

    # happy path
    def test_retrieve_post_content(self):
        # create mock request
        request = reddit_pb2.Post(id=mock_post_id)

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        # retrieve the post
        response = self.servicer.RetrievePostContent(request, mock_context)

        # check if the post is retrieved
        self.assertEqual(response.id, mock_post_id)
        self.assertEqual(response.content, "Test Post Content")

    # upvote non-existent post
    def test_retrieve_nonexistent_post_content(self):
        # create mock request
        request = reddit_pb2.Post(id="nonexistent")

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        # should produce error message
        self.servicer.RetrievePostContent(request, mock_context)
        mock_context.set_details.assert_called_with("Post not found!")
        mock_context.set_code.assert_called_with(grpc.StatusCode.NOT_FOUND)


if __name__ == "__main__":
    unittest.main()
