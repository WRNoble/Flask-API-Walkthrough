import datetime

from peewee import *

class Course(Model):
    title = CharField()
    url = CharField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = Database

class Review(Model):
    course = ForeignKeyField(Course, related_name='review_set')
    rating = integerField()
    comment = TextField(default='')
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = Database

def initialize():
    Database.connect()
    Database.create_tables([Course, Review], safe=True)
    Database.close()