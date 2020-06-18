import datetime

from peewee import *

class Course(Model):
    title = CharField()
    url = CharField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)