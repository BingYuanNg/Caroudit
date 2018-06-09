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

def checkIfEmpty(topic):
	if topic == "":
		raise CustomError('Topic is empty')
	else:
		return topic

def checkIfLengthExceed(topic,length=255):
	if len(topic) > 255:
		raise CustomError('Topic exceed length 255')

def sortVote(vote_lookup, topics):
	for i in range(len(vote_lookup)-1,0,-1):
		if topics[vote_lookup[i]].votes <= topics[vote_lookup[i-1]].votes:
			continue
		for j in range(i):
			if topics[vote_lookup[i]].votes > topics[vote_lookup[j]].votes:
				vote_lookup[j],vote_lookup[j+1:i+1] = vote_lookup[i],vote_lookup[j:i]
				break

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