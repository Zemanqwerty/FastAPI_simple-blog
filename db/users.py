from curses import meta
from email.policy import default
from enum import unique
import sqlalchemy
from .base import metadata
import datetime

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id_user', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column('username', sqlalchemy.String, unique=True),
    sqlalchemy.Column('password', sqlalchemy.String),
    sqlalchemy.Column('created_at', sqlalchemy.DateTime, default=datetime.datetime.utcnow),
)