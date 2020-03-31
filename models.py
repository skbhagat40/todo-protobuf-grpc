from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Todo(Base):
    __tablename__ = 'todos'

    id = Column('id', Integer, primary_key=True)
    title = Column('title', String)
    status = Column('status', Boolean)
    created_at = Column('created_at', DateTime, nullable=True)
    last_updated_at = Column('last_updated_at', DateTime, nullable=True)
