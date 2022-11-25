import pymongo

client = pymongo.MongoClient("mongodb+srv://maharanasunil1843:Sunil131096@cluster0.tmhnkhm.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data1 = [
    {
        "item" : "canvas",
        "qty": 100,
        "size": {"h": 28, "w": 35.5, "uom": "cm"},
        "status": "A"
    },
    {
        "item" : "journal",
        "qty": 25,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status" : "A"
    },
    {
        "item" : "mat",
        "qty": 85,
        "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
        "status": "A"
    },
    {
        "item" : "mousepad",
        "qty": 25,
        "size": {"h": 19, "w": 22.85, "uom": "cm"},
        "status": "P"
    },
    {
        "item" : "notebook",
        "qty": 50,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "P"
    },
    {
        "item" : "paper",
        "qty": 100,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "D"
    },
    {
        "item" : "planner",
        "qty": 75,
        "size": {"h": 22.85, "w": 30, "uom": "cm"},
        "status": "D"
    },
    {
        "item" : "postcard",
        "qty": 45,
        "size": {"h": 10, "w": 15.25, "uom": "cm"},
        "status": "A"
    },
    {
        "item" : "sketchbook",
        "qty": 80,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "D"
    },
    {
        "item": "sketch pad",
        "qty": 95,
        "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
        "status": "A"
    }
]
database = client["inventory"]
collection1 = database["table1"]
#collection1.insert_many(data1)

#d1 = collection1.find()
#for i in d1:
#    print(i)

#d2 = collection1.find({'status' : 'A'}) #only specific requirement
#for i in d2:
#    print(i)

#d3 = collection1.find({'status' : {'$in':['A', 'P']}}) # "$in" = or condition for matching cases in a single column
#for i in d3:
#    print(i)

#d4 = collection1.find({'status' : {'$gt' : 'C'}}) # "$gt" = greater than
#for i in d4:
#    print(i)

#d5 = collection1.find({'qty' : {'$gte': 70}}) # '$gte' = greater than or equal to
#for i in d5:
#    print(i)

#d6 = collection1.find({'item': 'sketch pad', 'qty': 95}) #applying conditions of multiple columns, give results if both the conditions are satisfied.
#for i in d6:
#    print(i)

#d7 = collection1.find({'item' : 'sketch pad', 'qty': {'$gte' : 75}}) #both conditions should be satisfied, equivalent to and condition.
#for i in d7:
#    print(i)

#d8 = collection1.find({'$or': [{'item' : 'sketch pad'}, {'qty': {'$gte' : 75}}]}) #equivalent to or condition for different columns.
#for i in d8:
#    print(i)

#collection1.update_one({'item': 'canvas'}, {'$set': {'item': 'pen'}}) #'$set' is a reserved keyword for updating documents in a given collection
#d9 = collection1.find()
#for i in d9:
#    print(i)

#collection1.delete_one({'item': 'journal'}) #delets data one by one
#d10 = collection1.find()
#for i in d10:
#    print(i)