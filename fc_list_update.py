import re

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('mongodb+srv://jungso:post9169@cluster0.kbds79b.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

db.fc_list_update.drop()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://franchise.ftc.go.kr/mnu/00013/program/userRqst/list.do?searchCondition=&searchKeyword=&column=brd&selUpjong=&selIndus=&pageUnit=20000&pageIndex=1',
    headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select('#frm > table > tbody > tr')
for pp in title:
    try:
        w = pp.select_one('td:nth-child(2) > a')["onclick"].split('firMstSn=')[1][:6]
        z = re.sub(r"[^0-9]", "", w)
        a = pp.select_one('td:nth-child(2) > a').text.strip()
        b = pp.select_one('td:nth-child(3) > a').text.strip()
        c = pp.select_one('td:nth-child(4)').text.strip()
        d = pp.select_one('td:nth-child(5)').text.strip()
        e = pp.select_one('td:nth-child(6)').text.strip()
        f = pp.select_one('td:nth-child(7)').text.strip()

        doc = {
            'z': z,
            '상호': a,
            '영업표지': b,
            '대표자': c,
            '등록번호': d,
            '최초등록일': e,
            '업종': f,
        }
        db.fc_list_update.insert_one(doc)
    except:
        pass
