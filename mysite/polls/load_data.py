import sys
import os
import csv
import django
from models import Player

# Full path to your django project directory
djangoproject = "/Users/Emanon805/Desktop/TIY/week4/day2/homework/arsenal-app/mysite/polls"
sys.path.append(djangoproject)
django.setup()
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


PATH = 'invincibles.csv'

with open(PATH, 'r') as f:
    catergories = {'fieldnames': ('kit_num', 'name', 'pos', 'dob', 'nat', 'apps', 'goals', 'assists', 'mins'), 'delimiter': ','}
    reader = csv.DictReader(f, **catergories)
    next(reader, None)

    for row in reader:
        p = Player()
        print(p)
        p.kit_num = row['kit_num']
        p.name = row['name']
        p.pos = row['pos']
        p.dob = row['dob']
        p.nat = row['nat']
        p.apps = row['apps']
        p.goals = row['goals']
        p.assists = row['assists']
        p.mins = row['mins']
        p.save()
