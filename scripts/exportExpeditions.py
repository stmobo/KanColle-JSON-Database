import json
import csv
import sys
import os

script_dir = os.path.dirname(__file__) # don't run this anywhere but scripts/

# Argument 1: CSV file with translated names.
#  Ensure that you have columns 'id' 'romaji' 'kana' 'chinese' 'kanji' and 'english'.
#  dumpnames.py outputs these so you should be fine.
# Argument 2: Input JSON file with original data.
#  These are the files in /db.
# Argument 3: Output JSON file to write to.
#
# The script uses the ID parameter to match JSON objects to CSV rows, so
# they should be the same.

csvlist = {}

with open(os.path.join(script_dir, '..\csv\expeditions.csv'), 'r', encoding='utf-8') as csv_in:
    reader = csv.DictReader(csv_in)
    for row in reader:
        obj = {
            'id': int(row['id']),
            'name': {
                'ja_jp': row['ja_jp'],
                'english': row['english']
            },
            'time': int(row['time']),
            'composition': row['reqComposition'],
            'level': {
                'flag': int(row['reqFlagLevel']),
                'combined': int(row['reqCombinedLevel'])
            },
            'drum': {
                'items': int(row['reqDrum']),
                'carriers': int(row['reqDrumCarriers'])
            },
            'exp': {
                'ship': int(row['shipExp']),
                'hq': int(row['hqExp'])
            },
            'resource': {
                'fuel': int(row['fuel']),
                'ammo': int(row['ammo']),
                'steel': int(row['steel']),
                'bauxite': int(row['baux'])
            },
            'normal_item': {
                'type': row['item'],
                'count': int(row['itemCount'])
            },
            'gs_item': {
                'type': row['gsItem'],
                'count': int(row['gsItemCount'])
            },
            'consum': {
                'fuel': float(row['fuelConsum']) / 10,
                'anmmo': float(row['ammoConsum']) / 10
            }
        }
        csvlist[int(row['id'])] = obj

        
with open(os.path.join(script_dir, '..\json-out\expeditions.json'), 'w', encoding='utf-8') as json_out:
    for idx in csvlist:
        obj = csvlist[idx]
        json_out.write(json.dumps(obj, ensure_ascii=False))
        json_out.write('\n')