import csv
import json

csvfile = open('invincibles.csv', 'r')
jsonfile = open('invincibles.json', 'w')

fieldnames = ('kit_num', 'name', 'pos', 'dob', 'nat', 'apps', 'goals', 'assists', 'mins')
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
