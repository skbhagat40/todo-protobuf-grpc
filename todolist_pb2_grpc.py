# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import todolist_pb2 as todolist__pb2


class TodoListStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAllTodos = channel.unary_unary(
        '/TodoList/GetAllTodos',
        request_serializer=todolist__pb2.ListTodosRequest.SerializeToString,
        response_deserializer=todolist__pb2.ListTodosResponse.FromString,
        )
    self.CreateTodo = channel.unary_unary(
        '/TodoList/CreateTodo',
        request_serializer=todolist__pb2.CreateTodoRequest.SerializeToString,
        response_deserializer=todolist__pb2.CreateTodoResponse.FromString,
        )
    self.EditTodo = channel.unary_unary(
        '/TodoList/EditTodo',
        request_serializer=todolist__pb2.EditTodoRequest.SerializeToString,
        response_deserializer=todolist__pb2.EditTodoResponse.FromString,
        )
    self.DeleteTodo = channel.unary_unary(
        '/TodoList/DeleteTodo',
        request_serializer=todolist__pb2.DeleteTodoRequest.SerializeToString,
        response_deserializer=todolist__pb2.DeleteTodoResponse.FromString,
        )
    self.UpdateTodoStatus = channel.unary_unary(
        '/TodoList/UpdateTodoStatus',
        request_serializer=todolist__pb2.UpdateTodoStatusRequest.SerializeToString,
        response_deserializer=todolist__pb2.UpdateTodoStatusResponse.FromString,
        )


class TodoListServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetAllTodos(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateTodo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EditTodo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteTodo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateTodoStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TodoListServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAllTodos': grpc.unary_unary_rpc_method_handler(
          servicer.GetAllTodos,
          request_deserializer=todolist__pb2.ListTodosRequest.FromString,
          response_serializer=todolist__pb2.ListTodosResponse.SerializeToString,
      ),
      'CreateTodo': grpc.unary_unary_rpc_method_handler(
          servicer.CreateTodo,
          request_deserializer=todolist__pb2.CreateTodoRequest.FromString,
          response_serializer=todolist__pb2.CreateTodoResponse.SerializeToString,
      ),
      'EditTodo': grpc.unary_unary_rpc_method_handler(
          servicer.EditTodo,
          request_deserializer=todolist__pb2.EditTodoRequest.FromString,
          response_serializer=todolist__pb2.EditTodoResponse.SerializeToString,
      ),
      'DeleteTodo': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteTodo,
          request_deserializer=todolist__pb2.DeleteTodoRequest.FromString,
          response_serializer=todolist__pb2.DeleteTodoResponse.SerializeToString,
      ),
      'UpdateTodoStatus': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateTodoStatus,
          request_deserializer=todolist__pb2.UpdateTodoStatusRequest.FromString,
          response_serializer=todolist__pb2.UpdateTodoStatusResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'TodoList', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
