# lol forgot the suffix ids
import sys
import json
import os


script_dir = os.path.dirname(__file__) # don't run this anywhere but scripts/
idSuffixMap = {}

with open(sys.argv[1], 'r', encoding='utf-8') as json_in:
    for line in json_in:
        obj = json.loads(line)
        idSuffixMap[obj['id']] = obj['name'].get('suffix');
        print(str(obj['id']) + ": suffix " + str(obj['name'].get('suffix')))
        
with open(os.path.join(script_dir, '..\db\ships.json'), 'r', encoding='utf-8') as json_in, open(os.path.join(script_dir, '..\json-out\ships.json'), 'w', encoding='utf-8') as json_out:
    for line in json_in:
        obj = json.loads(line)
        obj['name']['suffix'] = idSuffixMap[obj['id']];
        json_out.write(json.dumps(obj, ensure_ascii=False))
        json_out.write('\n')