from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Todo(Base):
    __tablename__ = 'todos'

    id = Column('id', Integer, primary_key=True)
    title = Column('title', String)
    status = Column('status', Boolean, default=False)
    created_at = Column('created_at', TIMESTAMP, nullable=True)
    last_updated_at = Column('last_updated_at', TIMESTAMP, nullable=True)
