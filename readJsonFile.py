import json


# Reading data back
with open('/Users/munperum/PycharmProjects/training/data/data.json', 'r') as f:
     data = json.load(f)

print(data)

f.close()