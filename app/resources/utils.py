from flask import request
import urllib

class CustomError(Exception):
	def __init__(self, m):
		self.message = m
	def __str__(self):
		return self.message

def checkIfExist(topics, topic_id):
	if topic_id not in topics :
		raise CustomError('Topic id does not exist')
	return  True

def checkIfEmpty(topic):
	if topic == "":
		raise CustomError('Topic is empty')
	else:
		return topic

def checkIfLengthExceed(topic,length=255):
	if len(topic) > 255:
		raise CustomError('Topic exceed length 255')

def sortVote(vote_lookup, topics):
	for i in vote_lookup:
		j = vote_lookup.index(i)
		#i is not the first element
		while j>0:
			#not in order
			if topics[vote_lookup[j-1]].votes < topics[vote_lookup[j]].votes:
				#swap
				vote_lookup[j-1],vote_lookup[j] = vote_lookup[j],vote_lookup[j-1]
			else:
				#in order
				break
			j = j-1

def checkIfSortable(sortable, option):
	if option not in sortable:
		raise CustomError('Wrong sort option')
	else:
		return option

def createPaginate(offset,limit,count):
	print(offset,limit,count)
	paging = {}
	query = {}

	if count >= offset + limit :
		query = {
			'offset' : offset+limit,
			'limit' : limit 
		}
		paging['next'] = "{}?{}".format(request.base_url, urllib.parse.urlencode(query))
		
	if offset - limit > 0:
		prev_offset = offset - limit;
		if prev_offset < 1 :
			prev_offset = 1
		query = {
			'offset' : prev_offset,
			'limit' : limit 
		}
		paging['prev'] = "{}?{}".format(request.base_url, urllib.parse.urlencode(query))
	
	return paging