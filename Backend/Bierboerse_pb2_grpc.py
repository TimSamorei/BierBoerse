# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Bierboerse_pb2 as Bierboerse__pb2


class BierboerseStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.addBeverage = channel.unary_unary(
                '/de.hadiko.vev.k2.bierboerse.Bierboerse/addBeverage',
                request_serializer=Bierboerse__pb2.AddRequest.SerializeToString,
                response_deserializer=Bierboerse__pb2.AddReply.FromString,
                )
        self.updateBeverage = channel.unary_unary(
                '/de.hadiko.vev.k2.bierboerse.Bierboerse/updateBeverage',
                request_serializer=Bierboerse__pb2.UpdateRequest.SerializeToString,
                response_deserializer=Bierboerse__pb2.UpdateReply.FromString,
                )
        self.getBeverage = channel.unary_unary(
                '/de.hadiko.vev.k2.bierboerse.Bierboerse/getBeverage',
                request_serializer=Bierboerse__pb2.GetRequest.SerializeToString,
                response_deserializer=Bierboerse__pb2.GetReply.FromString,
                )


class BierboerseServicer(object):
    """Missing associated documentation comment in .proto file."""

    def addBeverage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateBeverage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getBeverage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BierboerseServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'addBeverage': grpc.unary_unary_rpc_method_handler(
                    servicer.addBeverage,
                    request_deserializer=Bierboerse__pb2.AddRequest.FromString,
                    response_serializer=Bierboerse__pb2.AddReply.SerializeToString,
            ),
            'updateBeverage': grpc.unary_unary_rpc_method_handler(
                    servicer.updateBeverage,
                    request_deserializer=Bierboerse__pb2.UpdateRequest.FromString,
                    response_serializer=Bierboerse__pb2.UpdateReply.SerializeToString,
            ),
            'getBeverage': grpc.unary_unary_rpc_method_handler(
                    servicer.getBeverage,
                    request_deserializer=Bierboerse__pb2.GetRequest.FromString,
                    response_serializer=Bierboerse__pb2.GetReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'de.hadiko.vev.k2.bierboerse.Bierboerse', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Bierboerse(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def addBeverage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/de.hadiko.vev.k2.bierboerse.Bierboerse/addBeverage',
            Bierboerse__pb2.AddRequest.SerializeToString,
            Bierboerse__pb2.AddReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateBeverage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/de.hadiko.vev.k2.bierboerse.Bierboerse/updateBeverage',
            Bierboerse__pb2.UpdateRequest.SerializeToString,
            Bierboerse__pb2.UpdateReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getBeverage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/de.hadiko.vev.k2.bierboerse.Bierboerse/getBeverage',
            Bierboerse__pb2.GetRequest.SerializeToString,
            Bierboerse__pb2.GetReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
