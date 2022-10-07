import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["WKK_XXX"]
ban_user = mydb["ban_user"]
image_library = mydb["image_library"]
user_library = mydb["user_library"]
rank = mydb["rank"]


def find(mycol, value):
    return bool(mycol.find({}, {value}))
