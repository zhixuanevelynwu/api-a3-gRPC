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

mock_post_id = "0"


class TestRetrieveTopNComments(unittest.TestCase):
    def setUp(self):
        self.servicer = reddit_server.RedditServicer()

    # happy path
    # def test_retrieve_top_N_comments(self):
    #     # create mock request
    #     request = reddit_pb2.RetrieveTopNCommentsRequest(id=mock_post_id, N=10)

    #     # create a mock context
    #     mock_context = unittest.mock.Mock()
    #     mock_context.set_code = unittest.mock.Mock()
    #     mock_context.set_details = unittest.mock.Mock()

    #     # retrieve the post
    #     response = self.servicer.RetrieveTopNComments(request, mock_context)

    #     # check if the post is retrieved
    #     print(response)

    # upvote non-existent post
    def test_retrieve_nonexistent_post_content(self):
        pass


if __name__ == "__main__":
    unittest.main()
