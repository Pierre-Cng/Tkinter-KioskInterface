'''import json

with open('data.json') as f:
    d = json.load(f)
print(d['address']['city'])'''
id = int('0000047A', 16)
data = ['06', '00', '00', '00', '00', '00', '0A']
data = [int(x, 16) for x in data]
print(id, data)