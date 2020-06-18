import datetime

from peewee import *

class Course(Model):
    title = CharField()
    url = CharField(unique=True)