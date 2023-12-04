'''
This file implements a high level function that
    1. retrieves a post
    2. retrieves the most upvoted comment under this post
    3. expands the most upvoted comment
    4. returns the most upvoted reply under the most upvoted comment, or None if there are no comments or
no replies under the most upvoted one.
''' 

def top_reply_under_top_comment(client, post_id):
    # check if requested post exist
    post = client.retrieve_post_content(post_id)
    if not post:
        return None
    
    # retrieve the most upvoted comment under this post
    comments_response = client.retrieve_top_n_comments(post_id, 1)
    if not comments_response.comments_with_has_replies:
        return None

    # get the most upvoted reply
    top_comment = comments_response.comments_with_has_replies[0].comment
    replies_response = client.expand_comment_branch(top_comment.id, 1)

    # check if there are replies. if so, return the first reply
    if replies_response.comments_with_replies and replies_response.comments_with_replies[0].replies:
        return replies_response.comments_with_replies[0].comment
    else:
        return None



