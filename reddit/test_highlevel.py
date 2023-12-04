import unittest
import reddit_client
import reddit_server
import reddit_pb2
from db import posts, comments
from unittest.mock import patch, Mock
from highlevel import top_reply_under_top_comment

class TestRetrieveAndProcessPost(unittest.TestCase):
    def setUp(self):
        self.servicer = reddit_server.RedditServicer()

    @patch('reddit_client.RedditClient')  
    def test_highlevel_function(self, mock_client):
        # create a mock context
        mock_context = unittest.mock.Mock()
        mock_context.set_code = unittest.mock.Mock()
        mock_context.set_details = unittest.mock.Mock()

        # set up mock client
        mock_post_id = "0"
        top_comment_id = '0'
        mock_client.retrieve_post_content.return_value = self.servicer.RetrievePostContent(reddit_pb2.RetrievePostRequest(id=mock_post_id), mock_context)
        mock_client.retrieve_top_n_comments.return_value = self.servicer.RetrieveTopNComments(reddit_pb2.RetrieveTopNCommentsRequest(id=mock_post_id, N=1), mock_context)
        mock_client.expand_comment_branch.return_value = self.servicer.ExpandCommentBranch(reddit_pb2.ExpandCommentBranchRequest(id=mock_post_id, N=1), mock_context)

        # call high level function
        response = top_reply_under_top_comment(mock_client, mock_post_id)

        # Check that the client methods were called correctly
        mock_client.retrieve_post_content.assert_called_once_with(mock_post_id)
        mock_client.retrieve_top_n_comments.assert_called_once_with(mock_post_id, 1)
        mock_client.expand_comment_branch.assert_called_once_with(top_comment_id, 1)

        # Assert that the most upvoted reply is returned
        self.assertEqual(response.id, "100")
        self.assertEqual(response.score, 0)

   
if __name__ == "__main__":
    unittest.main()
