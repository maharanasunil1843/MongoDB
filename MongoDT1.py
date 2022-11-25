import pymongo

client = pymongo.MongoClient("mongodb+srv://maharanasunil1843:Sunil131096@cluster0.tmhnkhm.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data = {
    "name": "sunil",
    "mail_id": "maharanasunil1843@gmail.com",
    "subject": ["data science", "big data", "data analytics"]
}

list_of_records = [
    {
        'company name': 'iNeuron',
        'product': 'Affordable AI',
        'courseOffered': 'Machine Learning ith Deployment'
    },
    {
        'company name': 'iNeuron',
        'product': 'Affordable AI',
        'courseOffered': 'Deep Learning for NLP and Computer Vision'
    },
    {
        'company name': 'iNeuron',
        'product': 'Affordable AI',
        'courseOffered': 'Data Science Masters Program'
    }
]

database = client['myinfo']
collection = database['sunil']
#collection.insert_one(data)
#collection.insert_many(list_of_records)

data1 = {
	"id": "0001",
	"type": "donut",
	"name": "Cake",
	"ppu": 0.55,
	"batters":
		{
			"batter":
				[
					{ "id": "1001", "type": "Regular" },
					{ "id": "1002", "type": "Chocolate" },
					{ "id": "1003", "type": "Blueberry" },
					{ "id": "1004", "type": "Devil's Food" }
				]
		},
	"topping":
		[
			{ "id": "5001", "type": "None" },
			{ "id": "5002", "type": "Glazed" },
			{ "id": "5005", "type": "Sugar" },
			{ "id": "5007", "type": "Powdered Sugar" },
			{ "id": "5006", "type": "Chocolate with Sprinkles" },
			{ "id": "5003", "type": "Chocolate" },
			{ "id": "5004", "type": "Maple" }
		]
}
collection1 = database['dpkt']
#collection1.insert_one(data1)

#record = collection.find()
#for i in record:
#    print(i)

#record1 = collection1.find()
#for i in record1:
#    print(i)

#record2 = collection.find({"company name": 'iNeuron'}) #search where 'company name' = 'iNeuron'
#for i in record2:
#    print(i)

record3 = collection.find({"courseOffered" : {"$gt" : "E"}}) #stating a condition inside a condition.
for i in record3:
	print(i)
