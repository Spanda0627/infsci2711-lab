from pymongo import MongoClient, errors


try:
	'''Connect with local mongdb'''
	# MongoClient = MongoClient('localhost',27017)

	'''Connect with mongdb cluster'''
	MongoClient = MongoClient("mongodb://yfamy123:amy920420@cluster0-shard-00-00-fnmen.mongodb.net:27017,cluster0-shard-00-01-fnmen.mongodb.net:27017,cluster0-shard-00-02-fnmen.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")

	print("Connect successfully!")
except errors.ConnectionFailure:
   print("Could not connect to MongoDB")

print("Show database", MongoClient.database_names())

'''Change database'''
database = MongoClient.test

'''Get collection name'''
collection = database.collection_names(include_system_collections=False)

for collect in collection:
    print(collect)

'''Get collection restaurants'''
restaurants = database.restaurants

'''Print one sample'''
print(restaurants.find_one())

'''Print one sample with contrain'''
print(restaurants.find_one({ "name": "Wendy'S" }))