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


class TestExpandCommentBranch(unittest.TestCase):
    def setUp(self):
        self.servicer = reddit_server.RedditServicer()

    # happy path
    def test_expand_comment_branch(self):
        # create mock request
        request = reddit_pb2.ExpandCommentBranchRequest(id="0", N=10)

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        # expand the comment branch
        response = self.servicer.ExpandCommentBranch(request, mock_context)

        # check length
        self.assertEqual(len(response.comments_with_replies), 10)

        # by construction of our dummy data, the first 5 comments have 1 reply each
        for i in range(5):
            self.assertEqual(len(response.comments_with_replies[i].replies), 1)

    # non-existent comment
    def test_expand_nonexistent_comment_branch(self):
        # create mock request
        request = reddit_pb2.ExpandCommentBranchRequest(id="nonexistent", N=10)

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        # expand the comment branch
        self.servicer.ExpandCommentBranch(request, mock_context)

        # should produce error message
        mock_context.set_details.assert_called_with("Parent comment not found!")
        mock_context.set_code.assert_called_with(grpc.StatusCode.NOT_FOUND)


if __name__ == "__main__":
    unittest.main()
