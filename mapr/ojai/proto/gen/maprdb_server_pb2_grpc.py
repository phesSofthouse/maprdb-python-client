# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mapr.ojai.proto.gen.maprdb_server_pb2 as maprdb__server__pb2


class MapRDbServerStub(object):
    """=============================================//
    RPC calls exported from the service    //
    =============================================//
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/com.mapr.data.db.MapRDbServer/Ping',
                request_serializer=maprdb__server__pb2.PingRequest.SerializeToString,
                response_deserializer=maprdb__server__pb2.PingResponse.FromString,
                )
        self.CreateTable = channel.unary_unary(
                '/com.mapr.data.db.MapRDbServer/CreateTable',
                request_serializer=maprdb__server__pb2.CreateTableRequest.SerializeToString,
                response_deserializer=maprdb__server__pb2.CreateTableResponse.FromString,
                )
        self.DeleteTable = channel.unary_unary(
                '/com.mapr.data.db.MapRDbServer/DeleteTable',
                request_serializer=maprdb__server__pb2.DeleteTableRequest.SerializeToString,
                response_deserializer=maprdb__server__pb2.DeleteTableResponse.FromString,
                )
        self.TableExists = channel.unary_unary(
                '/com.mapr.data.db.MapRDbServer/TableExists',
                request_serializer=maprdb__server__pb2.TableExistsRequest.SerializeToString,
                response_deserializer=maprdb__server__pb2.TableExistsResponse.FromString,
                )
        self.InsertOrReplace = channel.unary_unary(
                '/com.mapr.data.db.MapRDbServer/InsertOrReplace',
                request_serializer=maprdb__server__pb2.InsertOrReplaceRequest.SerializeToString,
                response_deserializer=maprdb__server__pb2.InsertOrReplaceResponse.FromString,
                )
        self.FindById = channel.unary_unary(
                '/com.mapr.data.db.MapRDbServer/FindById',
                request_serializer=maprdb__server__pb2.FindByIdRequest.SerializeToString,
                response_deserializer=maprdb__server__pb2.FindByIdResponse.FromString,
                )
        self.Find = channel.unary_stream(
                '/com.mapr.data.db.MapRDbServer/Find',
                request_serializer=maprdb__server__pb2.FindRequest.SerializeToString,
                response_deserializer=maprdb__server__pb2.FindResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/com.mapr.data.db.MapRDbServer/Update',
                request_serializer=maprdb__server__pb2.UpdateRequest.SerializeToString,
                response_deserializer=maprdb__server__pb2.UpdateResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/com.mapr.data.db.MapRDbServer/Delete',
                request_serializer=maprdb__server__pb2.DeleteRequest.SerializeToString,
                response_deserializer=maprdb__server__pb2.DeleteResponse.FromString,
                )


class MapRDbServerServicer(object):
    """=============================================//
    RPC calls exported from the service    //
    =============================================//
    """

    def Ping(self, request, context):
        """Ping RPC
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTable(self, request, context):
        """Admin RPCs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TableExists(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsertOrReplace(self, request, context):
        """CRUD RPCs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Find(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MapRDbServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=maprdb__server__pb2.PingRequest.FromString,
                    response_serializer=maprdb__server__pb2.PingResponse.SerializeToString,
            ),
            'CreateTable': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTable,
                    request_deserializer=maprdb__server__pb2.CreateTableRequest.FromString,
                    response_serializer=maprdb__server__pb2.CreateTableResponse.SerializeToString,
            ),
            'DeleteTable': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTable,
                    request_deserializer=maprdb__server__pb2.DeleteTableRequest.FromString,
                    response_serializer=maprdb__server__pb2.DeleteTableResponse.SerializeToString,
            ),
            'TableExists': grpc.unary_unary_rpc_method_handler(
                    servicer.TableExists,
                    request_deserializer=maprdb__server__pb2.TableExistsRequest.FromString,
                    response_serializer=maprdb__server__pb2.TableExistsResponse.SerializeToString,
            ),
            'InsertOrReplace': grpc.unary_unary_rpc_method_handler(
                    servicer.InsertOrReplace,
                    request_deserializer=maprdb__server__pb2.InsertOrReplaceRequest.FromString,
                    response_serializer=maprdb__server__pb2.InsertOrReplaceResponse.SerializeToString,
            ),
            'FindById': grpc.unary_unary_rpc_method_handler(
                    servicer.FindById,
                    request_deserializer=maprdb__server__pb2.FindByIdRequest.FromString,
                    response_serializer=maprdb__server__pb2.FindByIdResponse.SerializeToString,
            ),
            'Find': grpc.unary_stream_rpc_method_handler(
                    servicer.Find,
                    request_deserializer=maprdb__server__pb2.FindRequest.FromString,
                    response_serializer=maprdb__server__pb2.FindResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=maprdb__server__pb2.UpdateRequest.FromString,
                    response_serializer=maprdb__server__pb2.UpdateResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=maprdb__server__pb2.DeleteRequest.FromString,
                    response_serializer=maprdb__server__pb2.DeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.mapr.data.db.MapRDbServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MapRDbServer(object):
    """=============================================//
    RPC calls exported from the service    //
    =============================================//
    """

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mapr.data.db.MapRDbServer/Ping',
            maprdb__server__pb2.PingRequest.SerializeToString,
            maprdb__server__pb2.PingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mapr.data.db.MapRDbServer/CreateTable',
            maprdb__server__pb2.CreateTableRequest.SerializeToString,
            maprdb__server__pb2.CreateTableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteTable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mapr.data.db.MapRDbServer/DeleteTable',
            maprdb__server__pb2.DeleteTableRequest.SerializeToString,
            maprdb__server__pb2.DeleteTableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TableExists(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mapr.data.db.MapRDbServer/TableExists',
            maprdb__server__pb2.TableExistsRequest.SerializeToString,
            maprdb__server__pb2.TableExistsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InsertOrReplace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mapr.data.db.MapRDbServer/InsertOrReplace',
            maprdb__server__pb2.InsertOrReplaceRequest.SerializeToString,
            maprdb__server__pb2.InsertOrReplaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mapr.data.db.MapRDbServer/FindById',
            maprdb__server__pb2.FindByIdRequest.SerializeToString,
            maprdb__server__pb2.FindByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Find(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/com.mapr.data.db.MapRDbServer/Find',
            maprdb__server__pb2.FindRequest.SerializeToString,
            maprdb__server__pb2.FindResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mapr.data.db.MapRDbServer/Update',
            maprdb__server__pb2.UpdateRequest.SerializeToString,
            maprdb__server__pb2.UpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.mapr.data.db.MapRDbServer/Delete',
            maprdb__server__pb2.DeleteRequest.SerializeToString,
            maprdb__server__pb2.DeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
