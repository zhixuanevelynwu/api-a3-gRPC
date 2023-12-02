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

mock_comment_id = "0"


class TestVoteComment(unittest.TestCase):
    def setUp(self):
        self.servicer = reddit_server.RedditServicer()

    # happy path
    def test_upvote_comment(self):
        # create mock request
        request = reddit_pb2.VoteCommentRequest(id=mock_comment_id)

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        # get old upvote count
        old_upvote_count = db.comments[mock_comment_id].score

        self.servicer.UpvoteComment(request, mock_context)

        # check if the score is incremented
        self.assertEqual(db.comments[mock_comment_id].score, old_upvote_count + 1)

    # upvote non-existent comment
    def test_upvote_nonexistent_comment(self):
        # create mock request
        request = reddit_pb2.VoteCommentRequest(id="nonexistent")

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        self.servicer.UpvoteComment(request, mock_context)
        mock_context.set_details.assert_called_with("Comment not found!")
        mock_context.set_code.assert_called_with(grpc.StatusCode.NOT_FOUND)

    # happy path
    def test_downvote_post(self):
        # create mock request
        request = reddit_pb2.VoteCommentRequest(id=mock_comment_id)

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        # get old upvote count
        old_upvote_count = db.comments[mock_comment_id].score

        self.servicer.DownvoteComment(request, mock_context)

        # check if the score is incremented
        self.assertEqual(db.comments[mock_comment_id].score, old_upvote_count - 1)

    # downvote non-existent comment
    def test_downvote_nonexistent_post(self):
        # create mock request
        request = reddit_pb2.VoteCommentRequest(id="nonexistent")

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        self.servicer.DownvoteComment(request, mock_context)

        mock_context.set_details.assert_called_with("Comment not found!")
        mock_context.set_code.assert_called_with(grpc.StatusCode.NOT_FOUND)


if __name__ == "__main__":
    unittest.main()
