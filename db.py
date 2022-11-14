import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['AliOSS']
fileIndex = mydb['fileIndex']


def how_much(id) -> int:
	a = 0
	for i in fileIndex.find({"user_id": id}):
		a += 1
	return a