#!/usr/bin/env python3
import requests
import csv

url = "https://docs.google.com/spreadsheets/d/1qMChLyePUHpWYNUbzmhGY1haWMrMCN3s5ZCPwEa6kYw/export?format=csv"

csv_data = None
try:
    with open('metadata-cache.csv', 'r', encoding='utf8') as f:
        csv_data = f.readlines()
except IOError:
    pass

if not csv_data:
    resp = requests.get(url)
    assert resp.status_code == 200
    csv_data = resp.content.decode('utf8').splitlines()

    if True:
        f = open('metadata-cache.csv', 'w', encoding='utf8')
        f.write(resp.content.decode('utf8'))
        f.close()

reader = csv.DictReader(csv_data, delimiter=',')
for row in reader:
    if not row['Name']:
        continue
    print(row)

