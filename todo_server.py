import todolist_pb2
import todolist_pb2_grpc
import grpc
from concurrent import futures


class TodoListServicer(todolist_pb2_grpc.TodoListServicer):
    def __init__(self):
        self.todos = {}
        self.id = 1

    def GetAllTodos(self, request, context):
        response = todolist_pb2.ListTodosResponse(todos=self.todos.values())
        print('returning response', response)
        return response

    def CreateTodo(self, request, context):
        todo = request.todo
        todo.id = self.id
        self.id += 1
        self.todos[todo.id] = todo
        response = todolist_pb2.CreateTodoResponse(
            todo=todo, message='Todo Created Successfully')
        return response

    def EditTodo(self, request, context):
        todo = self.todos.get(request.id)
        todo.title = request.title
        return todolist_pb2.EditTodoResponse(todo = todo, message='Todo Edited Successfully')
    
    def DeleteTodo(self, request, context):
        del self.todos[request.id]
        return todolist_pb2.DeleteTodoResponse(message='Todo Deleted Successfully')
    
    def UpdateTodoStatus(self, request, context):
        todo = self.todos.get(request.id)
        todo.status = request.status
        return todolist_pb2.UpdateTodoStatusResponse(message='Todo Status Updated Successfully', todo=todo)

def create_server(server_address):
    server = grpc.server(futures.ThreadPoolExecutor())
    todolist_pb2_grpc.add_TodoListServicer_to_server(TodoListServicer(), server)
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
    
