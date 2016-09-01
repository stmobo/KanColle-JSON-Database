import json
import csv
import sys

# Argument 1: Input JSON file.
#  This is the file from /db.
# Argument 2: Output CSV file to write to.
#  The CSV file will have the columns 'id', 'romaji', 'kanji', 'kana', and 'chinese'.

with open(sys.argv[1], encoding='utf-8') as input_json, open(sys.argv[2], 'w', newline='', encoding='utf-8') as output_file:
    output_csv = csv.DictWriter(output_file, fieldnames=['id', 'romaji', 'kanji', 'kana', 'chinese'])
    for line in input_json:
        obj = json.loads(line)
        if 'name' in obj:
            name_obj = obj['name']
            output_csv.writerow({
                'id':       obj['id'],
                'romaji':   name_obj.get('ja_romaji', ''),
                'kanji':    name_obj.get('ja_jp', ''),
                'kana':     name_obj.get('ja_kana', ''),
                'chinese':  name_obj.get('zh_cn', '')
            })

        else:
            output_csv.writerow({
                'id':       obj['id'],
                'romaji':   obj.get('ja_romaji', ''),
                'kanji':    obj.get('ja_jp', ''),
                'kana':     obj.get('ja_kana', ''),
                'chinese':  obj.get('zh_cn', '')
            })
    