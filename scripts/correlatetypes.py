import json
import csv
import sys
import os

csvlist = {}
type_names = {}
item_types = {}

script_dir = os.path.dirname(__file__) # don't run this anywhere but scripts/

# read in item -> english item type name mappings
with open(os.path.join(script_dir, '..\csv\items.csv'), 'r', encoding='utf-8') as csv_in:
    reader = csv.DictReader(csv_in)
    for row in reader:
        csvlist[int(row['id'])] = {
            'english': row['english'],
            'type_name': row['type']
        }

# read in item id -> item type id mappings
with open(os.path.join(script_dir, '..\db\items.json'), 'r', encoding='utf-8') as json_in:
    for line in json_in:
        obj = json.loads(line)
        if obj['type'] not in item_types:
            item_types[obj['type']] = []
        item_types[obj['type']].append(obj['name']['english'])
        type_names[obj['type']] = csvlist[obj['id']]['type_name']
        
for idx in item_types:
    print("Type ID " + str(idx) + ": " + type_names[idx])
    for it2, item in enumerate(item_types[idx]):
        print(" " + str(it2) + ": " + item)
        
jsonlist = {}
        
# read in item type objects
with open(os.path.join(script_dir, '..\db\item_types.json'), 'r', encoding='utf-8') as json_in:
    for line in json_in:
        obj = json.loads(line)
        obj['name']['english'] = type_names[obj['id']]
        jsonlist[obj['id']] = obj
        
with open(os.path.join(script_dir, '..\json-out\item_types.json'), 'w', encoding='utf-8') as json_out:
    for idx in jsonlist:
        obj = jsonlist[idx]
        json_out.write(json.dumps(obj, ensure_ascii=False))
        json_out.write('\n')