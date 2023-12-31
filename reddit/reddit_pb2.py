# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reddit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0creddit.proto\x12\x06reddit\"\x12\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\"\x88\x02\n\x04Post\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x13\n\timage_url\x18\x04 \x01(\tH\x00\x12\x13\n\tvideo_url\x18\x05 \x01(\tH\x00\x12\x14\n\x07user_id\x18\x06 \x01(\tH\x01\x88\x01\x01\x12\r\n\x05score\x18\x07 \x01(\x05\x12%\n\x05state\x18\x08 \x01(\x0e\x32\x16.reddit.Post.PostState\x12\x18\n\x10publication_date\x18\t \x01(\t\"/\n\tPostState\x12\n\n\x06NORMAL\x10\x00\x12\n\n\x06LOCKED\x10\x01\x12\n\n\x06HIDDEN\x10\x02\x42\x07\n\x05mediaB\n\n\x08_user_id\"\xf6\x01\n\x07\x43omment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x18\n\x0eparent_post_id\x18\x02 \x01(\tH\x00\x12\x1b\n\x11parent_comment_id\x18\x03 \x01(\tH\x00\x12\x0f\n\x07user_id\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12\r\n\x05score\x18\x06 \x01(\x05\x12+\n\x05state\x18\x07 \x01(\x0e\x32\x1c.reddit.Comment.CommentState\x12\x18\n\x10publication_date\x18\x08 \x01(\t\"&\n\x0c\x43ommentState\x12\n\n\x06NORMAL\x10\x00\x12\n\n\x06HIDDEN\x10\x01\x42\x08\n\x06parent\"\x88\x01\n\x11\x43reatePostRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x13\n\timage_url\x18\x03 \x01(\tH\x00\x12\x13\n\tvideo_url\x18\x04 \x01(\tH\x00\x12\x14\n\x07user_id\x18\x05 \x01(\tH\x01\x88\x01\x01\x42\x07\n\x05mediaB\n\n\x08_user_id\"\x1d\n\x0fVotePostRequest\x12\n\n\x02id\x18\x01 \x01(\t\"!\n\x13RetrievePostRequest\x12\n\n\x02id\x18\x01 \x01(\t\"y\n\x14\x43reateCommentRequest\x12\x18\n\x0eparent_post_id\x18\x01 \x01(\tH\x00\x12\x1b\n\x11parent_comment_id\x18\x02 \x01(\tH\x00\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\tB\x08\n\x06parent\" \n\x12VoteCommentRequest\x12\n\n\x02id\x18\x01 \x01(\t\"4\n\x1bRetrieveTopNCommentsRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\t\n\x01N\x18\x02 \x01(\x05\"N\n\x15\x43ommentWithHasReplies\x12 \n\x07\x63omment\x18\x01 \x01(\x0b\x32\x0f.reddit.Comment\x12\x13\n\x0bhas_replies\x18\x02 \x01(\x08\"`\n\x1cRetrieveTopNCommentsResponse\x12@\n\x19\x63omments_with_has_replies\x18\x01 \x03(\x0b\x32\x1d.reddit.CommentWithHasReplies\"3\n\x1a\x45xpandCommentBranchRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\t\n\x01N\x18\x02 \x01(\x05\"X\n\x12\x43ommentWithReplies\x12 \n\x07\x63omment\x18\x01 \x01(\x0b\x32\x0f.reddit.Comment\x12 \n\x07replies\x18\x02 \x03(\x0b\x32\x0f.reddit.Comment\"X\n\x1b\x45xpandCommentBranchResponse\x12\x39\n\x15\x63omments_with_replies\x18\x01 \x03(\x0b\x32\x1a.reddit.CommentWithReplies2\xf5\x04\n\rRedditService\x12\x35\n\nCreatePost\x12\x19.reddit.CreatePostRequest\x1a\x0c.reddit.Post\x12\x33\n\nUpvotePost\x12\x17.reddit.VotePostRequest\x1a\x0c.reddit.Post\x12\x35\n\x0c\x44ownvotePost\x12\x17.reddit.VotePostRequest\x1a\x0c.reddit.Post\x12@\n\x13RetrievePostContent\x12\x1b.reddit.RetrievePostRequest\x1a\x0c.reddit.Post\x12>\n\rCreateComment\x12\x1c.reddit.CreateCommentRequest\x1a\x0f.reddit.Comment\x12<\n\rUpvoteComment\x12\x1a.reddit.VoteCommentRequest\x1a\x0f.reddit.Comment\x12>\n\x0f\x44ownvoteComment\x12\x1a.reddit.VoteCommentRequest\x1a\x0f.reddit.Comment\x12\x61\n\x14RetrieveTopNComments\x12#.reddit.RetrieveTopNCommentsRequest\x1a$.reddit.RetrieveTopNCommentsResponse\x12^\n\x13\x45xpandCommentBranch\x12\".reddit.ExpandCommentBranchRequest\x1a#.reddit.ExpandCommentBranchResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reddit_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USER']._serialized_start=24
  _globals['_USER']._serialized_end=42
  _globals['_POST']._serialized_start=45
  _globals['_POST']._serialized_end=309
  _globals['_POST_POSTSTATE']._serialized_start=241
  _globals['_POST_POSTSTATE']._serialized_end=288
  _globals['_COMMENT']._serialized_start=312
  _globals['_COMMENT']._serialized_end=558
  _globals['_COMMENT_COMMENTSTATE']._serialized_start=510
  _globals['_COMMENT_COMMENTSTATE']._serialized_end=548
  _globals['_CREATEPOSTREQUEST']._serialized_start=561
  _globals['_CREATEPOSTREQUEST']._serialized_end=697
  _globals['_VOTEPOSTREQUEST']._serialized_start=699
  _globals['_VOTEPOSTREQUEST']._serialized_end=728
  _globals['_RETRIEVEPOSTREQUEST']._serialized_start=730
  _globals['_RETRIEVEPOSTREQUEST']._serialized_end=763
  _globals['_CREATECOMMENTREQUEST']._serialized_start=765
  _globals['_CREATECOMMENTREQUEST']._serialized_end=886
  _globals['_VOTECOMMENTREQUEST']._serialized_start=888
  _globals['_VOTECOMMENTREQUEST']._serialized_end=920
  _globals['_RETRIEVETOPNCOMMENTSREQUEST']._serialized_start=922
  _globals['_RETRIEVETOPNCOMMENTSREQUEST']._serialized_end=974
  _globals['_COMMENTWITHHASREPLIES']._serialized_start=976
  _globals['_COMMENTWITHHASREPLIES']._serialized_end=1054
  _globals['_RETRIEVETOPNCOMMENTSRESPONSE']._serialized_start=1056
  _globals['_RETRIEVETOPNCOMMENTSRESPONSE']._serialized_end=1152
  _globals['_EXPANDCOMMENTBRANCHREQUEST']._serialized_start=1154
  _globals['_EXPANDCOMMENTBRANCHREQUEST']._serialized_end=1205
  _globals['_COMMENTWITHREPLIES']._serialized_start=1207
  _globals['_COMMENTWITHREPLIES']._serialized_end=1295
  _globals['_EXPANDCOMMENTBRANCHRESPONSE']._serialized_start=1297
  _globals['_EXPANDCOMMENTBRANCHRESPONSE']._serialized_end=1385
  _globals['_REDDITSERVICE']._serialized_start=1388
  _globals['_REDDITSERVICE']._serialized_end=2017
# @@protoc_insertion_point(module_scope)
