from mongoengine import *
connect('calculations')

class Base(Document):
	value1 = FloatField(required=True)
	value2 = FloatField(required=True)
	meta = {'allow_inheritance': True, 'collection': 'data'}

class Addition(Base):
	result = FloatField()
	method = StringField()

class Multiplication(Base):
	result = FloatField()
	method = StringField()

class Summation(Base):
	result = FloatField()
	method = StringField()