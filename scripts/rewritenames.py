import json
import csv
import sys

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

with open(sys.argv[2], 'r', encoding='utf-8') as csv_in:
    reader = csv.DictReader(csv_in)
    for row in reader:
        csvlist[int(row['id'])] = {
            'english': row['english'],
            'ja_romaji': row['romaji'],
            'ja_jp': row['kanji'],
            'ja_kana': row['kana'],
            'zh_cn': row['chinese']
        }
        
jsonlist = {}
        
with open(sys.argv[1], 'r', encoding='utf-8') as json_in:
    for line in json_in:
        obj = json.loads(line)
        obj['name'] = csvlist[obj['id']]
        jsonlist[obj['id']] = obj
        
with open(sys.argv[3], 'w', encoding='utf-8') as json_out:
    for idx in jsonlist:
        obj = jsonlist[idx]
        json_out.write(json.dumps(obj, ensure_ascii=False))
        json_out.write('\n')