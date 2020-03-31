from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from models import Todo
import sqlalchemy
from sqlalchemy.orm import mapper
from sqlalchemy.inspection import inspect
import datetime
from contextlib import contextmanager


@contextmanager
def open_session(Session):
    try:
        session = Session()
        yield session
    except Exception as e:
        session.rollback()
        raise
    finally:
        # session.expunge_all()
        session.close()


def return_dict(func):
    # takes an sqlalchemy object instance and returns a dict.
    def inner_func(*args, **kwargs):
        result = func(*args, **kwargs)
        return_dicts = []
        if isinstance(result, list):
            for r in result:
                return_dicts.append({c.key: getattr(r, c.key)
                                     for c in inspect(r).mapper.column_attrs})
            return return_dicts
        else:
            return {c.key: getattr(result, c.key)
                    for c in inspect(result).mapper.column_attrs}
    return inner_func


class QueryHelper():
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)

    @return_dict
    def get_all_todos(self):
        with open_session(self.Session) as session:
            return session.query(Todo).all()

    @return_dict
    def edit_todo(self, id, title):
        with open_session(self.Session) as session:
            todo = session.query(Todo).filter(Todo.id == id).one()
            todo.title = title
            session.commit()
            return todo

    @return_dict
    def update_status(self, id, status):
        with open_session(self.Session) as session:
            todo = session.query(Todo).filter(Todo.id == id).one()
            todo.status = status
            todo.last_updated_at = datetime.datetime.now()
            session.commit()
            return todo

    def delete_todo(self, id):
        with open_session(self.Session) as session:
            todo = session.query(Todo).filter(Todo.id == id).one()
            session.delete(todo)
            session.commit()

    @return_dict
    def create_todo(self, title):
        todo = Todo(title=title)
        with open_session(self.Session) as session:
            todo.created_at = datetime.datetime.now()
            session.add(todo)
            session.commit()
            return todo
