import todolist_pb2_grpc
import todolist_pb2
import grpc
TODO_OPTIONS = {1: lambda x: add_todo(), 2: lambda x: list_todos(),
                3: lambda x: delete_todo(), 4: lambda x: edit_todo(), 5: lambda x: update_status()}

def get_todo_id(keyword=None):
    todos = get_todos()
    todo_ids = {todo.id for todo in todos}
    todo_string = "\n".join([str(el.id) + '. ' + el.title for el in todos])
    while True:
        id = int(input('Enter the id of the todo you want to {} \n'.format(keyword) +
                    todo_string +"\n"))
        if id in todo_ids:
            break
        print('Please Choose a valid id \n')
    return id

def add_todo():
    title = input('Enter the Title \n')
    todo = todolist_pb2.Todo(title=title, status=False)
    response = stub.CreateTodo(todolist_pb2.CreateTodoRequest(todo=todo))
    print('response is', response)
    return todo


def get_todos():
    todos = stub.GetAllTodos(todolist_pb2.ListTodosRequest()).todos
    return todos

def list_todos():
    todos = get_todos()
    for todo in todos:
        print("*" * 10)
        print("Title : {}".format(todo.title))
        print("Status : {}".format(todo.status))
        print("Created_at : {}".format(todo.created_at))
        print("Last Updated at : {}".format(todo.last_updated_at))
        print("*" * 10)
        print('\n'*2)


def delete_todo():
    id = get_todo_id('delete')
    response = stub.DeleteTodo(todolist_pb2.DeleteTodoRequest(id=id))
    print('response', response.message)


def edit_todo():
    id = get_todo_id('edit')
    title = input("Enter the new title \n")
    response = stub.EditTodo(todolist_pb2.EditTodoRequest(id=id, title=title))
    print('response', response)

def update_status():
    STATUS_MAPPING = {1: True, 2: False}
    id = get_todo_id('update status')
    status = STATUS_MAPPING[int(input('Please choose 1. Complete 2. Incomplete \n'))]
    response = stub.UpdateTodoStatus(todolist_pb2.UpdateTodoStatusRequest(id=id, status=status))
    print('response is complete: ', response.todo.status)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        global stub
        stub = todolist_pb2_grpc.TodoListStub(channel)
        while True:
            choice = int(input("""Enter a choice
                              1. Add
                              2. List
                              3. Delete
                              4. Edit
                              5. Update Status
                              6. Exit \n"""))
            if choice == 6:
                break
            TODO_OPTIONS[choice](None)
        # todolist methods to be implemented goes here.
        # response = stub.GetGreeting(myService_pb2.GreetingRequest(name='Shailesh'))
        # print('response', response.response)


if __name__ == '__main__':
    run()
