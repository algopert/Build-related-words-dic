import pymongo
# _database, _collection

MONGODB_TIMEOUT = 1000
MONGODB_SOCKETTIMEOUT = 3000

URI_CONNECTION =  'mongodb://localhost:27017'    #'mongodb+srv://robyuri:1KamPSTmGEmcYpac@cluster0.yb2eg.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(URI_CONNECTION, connectTimeoutMS=MONGODB_TIMEOUT,socketTimeoutMS=MONGODB_SOCKETTIMEOUT)

print(client)
print("1111111111--------",client.list_database_names())

mydb = client["WordGame"]
mycol = mydb["demo_dicts"]


f = open('demo.csv', 'r')
word_list = f.read().splitlines()
f.close


for _word_pack in word_list:
    my_words = _word_pack.split(", ")
    _word ={"round":int(my_words[0]), "sample":my_words[1], "target":my_words[2]}
    
    # myquery = {"word": _word["word"],  "related": _word["related"]}
    print(_word)
    mycol.update_one(_word, {"$setOnInsert": _word}, upsert=True)
        
