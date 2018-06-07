from flask import request
import urllib

class CustomError(Exception):
	def __init__(self, m):
		self.message = m
	def __str__(self):
		return self.message

def checkIfEmpty(topic):
	if topic == "":
		raise CustomError('Topic is empty')
	else:
		return topic

def checkIfLengthExceed(topic,length=255):
	if len(topic) > 255:
		raise CustomError('Topic exceed length 255')
