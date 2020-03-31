import todolist_pb2
import todolist_pb2_grpc
import grpc
from concurrent import futures
from sqlalchemy import create_engine
import environment
import utils
from sqlalchemy.orm import class_mapper
import sqlalchemy


class TodoListServicer(todolist_pb2_grpc.TodoListServicer):
    def __init__(self):
        self.queryHelper = utils.QueryHelper(
            engine=create_engine(environment.DB_CONNECTION_STRING))

    def GetAllTodos(self, request, context):
        response = todolist_pb2.ListTodosResponse(
            todos=self.queryHelper.get_all_todos())
        return response

    def CreateTodo(self, request, context):
        todo = request.todo
        todo = self.queryHelper.create_todo(title=todo.title)
        response = todolist_pb2.CreateTodoResponse(
            todo=todo, message='Todo Created Successfully')
        return response

    def EditTodo(self, request, context):
        todo = self.queryHelper.edit_todo(request.id, request.title)
        return todolist_pb2.EditTodoResponse(todo=todo, message='Todo Edited Successfully')

    def DeleteTodo(self, request, context):
        self.queryHelper.delete_todo(request.id)
        return todolist_pb2.DeleteTodoResponse(message='Todo Deleted Successfully')

    def UpdateTodoStatus(self, request, context):
        todo = self.queryHelper.update_status(request.id, request.status)
        return todolist_pb2.UpdateTodoStatusResponse(message='Todo Status Updated Successfully', todo=todo)


def create_server(server_address):
    server = grpc.server(futures.ThreadPoolExecutor())
    todolist_pb2_grpc.add_TodoListServicer_to_server(
        TodoListServicer(), server)
    port = server.add_insecure_port(server_address)
    return server, port


def serve(server):
    server.start()
    server.wait_for_termination()


def main():
    server, unused_port = create_server('[::]:50051')
    serve(server)


if __name__ == '__main__':
    main()
