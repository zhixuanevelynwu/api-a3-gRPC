# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import reddit_pb2 as reddit__pb2


class RedditServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreatePost = channel.unary_unary(
                '/reddit.RedditService/CreatePost',
                request_serializer=reddit__pb2.Post.SerializeToString,
                response_deserializer=reddit__pb2.Post.FromString,
                )
        self.UpvotePost = channel.unary_unary(
                '/reddit.RedditService/UpvotePost',
                request_serializer=reddit__pb2.Post.SerializeToString,
                response_deserializer=reddit__pb2.Post.FromString,
                )
        self.DownvotePost = channel.unary_unary(
                '/reddit.RedditService/DownvotePost',
                request_serializer=reddit__pb2.Post.SerializeToString,
                response_deserializer=reddit__pb2.Post.FromString,
                )
        self.RetrievePostContent = channel.unary_unary(
                '/reddit.RedditService/RetrievePostContent',
                request_serializer=reddit__pb2.Post.SerializeToString,
                response_deserializer=reddit__pb2.Post.FromString,
                )
        self.CreateComment = channel.unary_unary(
                '/reddit.RedditService/CreateComment',
                request_serializer=reddit__pb2.Comment.SerializeToString,
                response_deserializer=reddit__pb2.Comment.FromString,
                )
        self.UpvoteComment = channel.unary_unary(
                '/reddit.RedditService/UpvoteComment',
                request_serializer=reddit__pb2.Comment.SerializeToString,
                response_deserializer=reddit__pb2.Comment.FromString,
                )
        self.DownvoteComment = channel.unary_unary(
                '/reddit.RedditService/DownvoteComment',
                request_serializer=reddit__pb2.Comment.SerializeToString,
                response_deserializer=reddit__pb2.Comment.FromString,
                )
        self.RetrieveTopComments = channel.unary_unary(
                '/reddit.RedditService/RetrieveTopComments',
                request_serializer=reddit__pb2.RetrieveTopCommentsRequest.SerializeToString,
                response_deserializer=reddit__pb2.RetrieveTopCommentsResponse.FromString,
                )


class RedditServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreatePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpvotePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownvotePost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrievePostContent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpvoteComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownvoteComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveTopComments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RedditServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreatePost': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePost,
                    request_deserializer=reddit__pb2.Post.FromString,
                    response_serializer=reddit__pb2.Post.SerializeToString,
            ),
            'UpvotePost': grpc.unary_unary_rpc_method_handler(
                    servicer.UpvotePost,
                    request_deserializer=reddit__pb2.Post.FromString,
                    response_serializer=reddit__pb2.Post.SerializeToString,
            ),
            'DownvotePost': grpc.unary_unary_rpc_method_handler(
                    servicer.DownvotePost,
                    request_deserializer=reddit__pb2.Post.FromString,
                    response_serializer=reddit__pb2.Post.SerializeToString,
            ),
            'RetrievePostContent': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrievePostContent,
                    request_deserializer=reddit__pb2.Post.FromString,
                    response_serializer=reddit__pb2.Post.SerializeToString,
            ),
            'CreateComment': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateComment,
                    request_deserializer=reddit__pb2.Comment.FromString,
                    response_serializer=reddit__pb2.Comment.SerializeToString,
            ),
            'UpvoteComment': grpc.unary_unary_rpc_method_handler(
                    servicer.UpvoteComment,
                    request_deserializer=reddit__pb2.Comment.FromString,
                    response_serializer=reddit__pb2.Comment.SerializeToString,
            ),
            'DownvoteComment': grpc.unary_unary_rpc_method_handler(
                    servicer.DownvoteComment,
                    request_deserializer=reddit__pb2.Comment.FromString,
                    response_serializer=reddit__pb2.Comment.SerializeToString,
            ),
            'RetrieveTopComments': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveTopComments,
                    request_deserializer=reddit__pb2.RetrieveTopCommentsRequest.FromString,
                    response_serializer=reddit__pb2.RetrieveTopCommentsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'reddit.RedditService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RedditService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreatePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reddit.RedditService/CreatePost',
            reddit__pb2.Post.SerializeToString,
            reddit__pb2.Post.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpvotePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reddit.RedditService/UpvotePost',
            reddit__pb2.Post.SerializeToString,
            reddit__pb2.Post.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownvotePost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reddit.RedditService/DownvotePost',
            reddit__pb2.Post.SerializeToString,
            reddit__pb2.Post.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrievePostContent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reddit.RedditService/RetrievePostContent',
            reddit__pb2.Post.SerializeToString,
            reddit__pb2.Post.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reddit.RedditService/CreateComment',
            reddit__pb2.Comment.SerializeToString,
            reddit__pb2.Comment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpvoteComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reddit.RedditService/UpvoteComment',
            reddit__pb2.Comment.SerializeToString,
            reddit__pb2.Comment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownvoteComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reddit.RedditService/DownvoteComment',
            reddit__pb2.Comment.SerializeToString,
            reddit__pb2.Comment.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveTopComments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reddit.RedditService/RetrieveTopComments',
            reddit__pb2.RetrieveTopCommentsRequest.SerializeToString,
            reddit__pb2.RetrieveTopCommentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
