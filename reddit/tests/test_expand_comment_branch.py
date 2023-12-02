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
    def DISABLED_test_expand_comment_branch(self):
        # create mock request
        request = reddit_pb2.ExpandCommentBranchRequest(id="0", N=1)

        # expand the comment branch
        response = self.servicer.ExpandCommentBranch(request, None)
        print(response)


if __name__ == "__main__":
    unittest.main()
