import sqlalchemy
from .base import metadata
import datetime

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id_user', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('username', sqlalchemy.String, unique=True),
    sqlalchemy.Column('hashed_password', sqlalchemy.String),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow),
)