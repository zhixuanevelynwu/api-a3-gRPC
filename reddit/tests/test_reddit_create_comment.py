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

mock_post_id = "0011"
mock_comment_id = "1100"


class TestCreateComment(unittest.TestCase):
    def setUp(self):
        self.servicer = reddit_server.RedditServicer()

    # uuid return constant value
    @patch("reddit_server.uuid.uuid4", return_value=mock_comment_id)
    # happy path
    def test_create_comment(self, mock_uuid):
        # create mock request
        mock_request = reddit_pb2.Comment(
            user_id="user0",
            parent_post_id=mock_post_id,
            content="Test Comment Content",
        )

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        # call servicer
        response = self.servicer.CreateComment(mock_request, mock_context)

        # check response
        self.assertEqual(response.id, mock_comment_id)
        self.assertEqual(response.content, mock_request.content)
        self.assertEqual(response.user_id, mock_request.user_id)
        self.assertEqual(response.score, 0)
        self.assertEqual(response.state, reddit_pb2.Comment.CommentState.NORMAL)
        self.assertEqual(response.parent_post_id, mock_request.parent_post_id)
        self.assertEqual(response.parent_comment_id, "")
        self.assertTrue(response.publication_date is not None)

    # create a comment with no content
    def test_create_invalid_comment_no_content(self):
        # create invalid mock request
        mock_request = reddit_pb2.Comment(
            user_id="user0",
            parent_post_id=mock_post_id,
        )

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        self.servicer.CreateComment(mock_request, mock_context)
        mock_context.set_details.assert_called_with("Invalid comment!")
        mock_context.set_code.assert_called_with(grpc.StatusCode.INVALID_ARGUMENT)

    # create a comment without valid parent
    def test_create_invalid_comment_no_parent(self):
        # create invalid mock request
        mock_request = reddit_pb2.Comment(
            user_id="user0",
            parent_post_id="nonexistent",
            content="Test Comment Content",
        )

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        self.servicer.CreateComment(mock_request, mock_context)
        mock_context.set_details.assert_called_with("Parent not found!")
        mock_context.set_code.assert_called_with(grpc.StatusCode.NOT_FOUND)


if __name__ == "__main__":
    unittest.main()
