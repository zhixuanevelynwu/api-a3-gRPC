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
    def test_retrieve_top_N_comments(self):
        # create mock request
        request = reddit_pb2.RetrieveTopNCommentsRequest(id=mock_post_id, N=10)

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        # retrieve the post
        response = self.servicer.RetrieveTopNComments(request, mock_context)

        # check if there are N comments as required
        self.assertEqual(len(response.comments), 10)

        # check if sorted in descending order by score
        current_min_score = float("inf")
        for comment in response.comments:
            self.assertTrue(comment.score <= current_min_score)
            current_min_score = comment.score
            assert comment.has_replies == True

    def test_retrieve_more_comments_than_exist(self):
        # create mock request
        request = reddit_pb2.RetrieveTopNCommentsRequest(id=mock_post_id, N=10000)

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        # retrieve the post
        response = self.servicer.RetrieveTopNComments(request, mock_context)

        # check if there are N comments as required
        self.assertEqual(len(response.comments), 100)

        # check if sorted in descending order by score
        current_min_score = float("inf")
        for comment in response.comments:
            self.assertTrue(comment.score <= current_min_score)
            current_min_score = comment.score

    # upvote non-existent post
    def test_retrieve_nonexistent_post_content(self):
        # create mock request
        request = reddit_pb2.RetrieveTopNCommentsRequest(id="nonexistent", N=10000)

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        # retrieve the post
        self.servicer.RetrieveTopNComments(request, mock_context)

        # should produce error message
        mock_context.set_details.assert_called_with("Post not found!")
        mock_context.set_code.assert_called_with(grpc.StatusCode.NOT_FOUND)


if __name__ == "__main__":
    unittest.main()
