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


class TestCreatePost(unittest.TestCase):
    def setUp(self):
        self.servicer = reddit_server.RedditServicer()

    # uuid return constant value
    @patch("reddit_server.uuid.uuid4", return_value=mock_post_id)
    # happy path
    def test_create_post(self, mock_uuid):
        # create mock request
        mock_request = reddit_pb2.CreatePostRequest(
            title="Test Post Title",
            content="Test Post Content",
            user_id="user1",
            image_url="./test.jpg",
        )

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        # call servicer
        response = self.servicer.CreatePost(mock_request, mock_context)

        # check response
        self.assertEqual(response.id, mock_post_id)
        self.assertEqual(response.title, mock_request.title)
        self.assertEqual(response.content, mock_request.content)
        self.assertEqual(response.user_id, mock_request.user_id)
        self.assertEqual(response.score, 0)
        self.assertEqual(response.state, reddit_pb2.Post.PostState.NORMAL)
        self.assertEqual(response.image_url, mock_request.image_url)
        self.assertEqual(response.video_url, "")
        self.assertTrue(response.publication_date is not None)

    # create a invalid post
    def test_create_invalid_post(self):
        # create invalid mock request
        mock_request = reddit_pb2.CreatePostRequest(
            title="Test Post Title",
            image_url="./test.jpg",
            video_url="./test.mp4",
        )

        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        self.servicer.CreatePost(mock_request, mock_context)
        mock_context.set_details.assert_called_with("Invalid post!")
        mock_context.set_code.assert_called_with(grpc.StatusCode.INVALID_ARGUMENT)


if __name__ == "__main__":
    unittest.main()
