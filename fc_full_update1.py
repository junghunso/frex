import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('mongodb+srv://jungso:post9169@cluster0.kbds79b.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

all_update_list = list(db.fc_update.find({}, {'_id': False}))
for m in all_update_list:
    z = m['z']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    url_give = "https://franchise.ftc.go.kr/mnu/00013/program/userRqst/view.do?firMstSn=" + z

    data = requests.get(url_give, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')


    # member

    title = soup.select('#frm > div:nth-child(13) > div > table:nth-child(4) > tbody > tr')
    for pp in title:
        try:
            aa = pp.select_one('td.noborder').text.strip()
            a = pp.select_one('td:nth-child(2)').text.strip()
            b = pp.select_one('td:nth-child(3)').text.strip()
            c = pp.select_one('td:nth-child(4)').text.strip()
            d = pp.select_one('td:nth-child(5)').text.strip()
            e = pp.select_one('td:nth-child(6)').text.strip()
            f = pp.select_one('td:nth-child(7)').text.strip()
            g = pp.select_one('td:nth-child(8)').text.strip()
            h = pp.select_one('td:nth-child(9)').text.strip()
            i = pp.select_one('td:nth-child(10)').text.strip()

            doc = {
                'z': z,
                'region': aa,
                'store_t1': a,
                'store_f1': b,
                'store_d1': c,
                'store_t2': d,
                'store_f2': e,
                'store_d2': f,
                'store_t3': g,
                'store_f3': h,
                'store_d3': i,
            }
            db.fc_members.insert_one(doc)
        except:
            pass

    # Arev

    title = soup.select('#frm > div:nth-child(13) > div > table:nth-child(8) > tbody > tr')
    for pp in title:
        try:
            i = pp.select_one('td.noborder').text.strip()
            a = pp.select_one('td:nth-child(2)').text.strip()
            b = pp.select_one('td:nth-child(3)').text.strip()
            c = pp.select_one('td:nth-child(4)').text.strip()

            doc = {
                'z': z,
                'i': i,
                'a': a,
                'b': b,
                'c': c,
            }
            db.fc_Arev.insert_one(doc)
        except:
            pass

    # Change

    title = soup.select('#frm > div:nth-child(13) > div > table:nth-child(6) > tr')
    for pp in title:
        try:
            a = pp.select_one('td.noborder').text.strip()
            b = pp.select_one('td:nth-child(2)').text.strip()
            c = pp.select_one('td:nth-child(3)').text.strip()
            d = pp.select_one('td:nth-child(4)').text.strip()
            e = pp.select_one('td:nth-child(5)').text.strip()

            doc = {
                'z': z,
                'a': a,
                'b': b,
                'c': c,
                'd': d,
                'e': e,
            }
            db.fc_change_num.insert_one(doc)
        except:
            pass

    # fs

    title = soup.select('#frm > div:nth-child(12) > div > table:nth-child(5) > tbody > tr:nth-child(2)')
    for pp in title:
        try:
            y = pp.select_one('td.noborder').text.strip()
            a = pp.select_one('td:nth-child(2)').text.strip()
            b = pp.select_one('td:nth-child(3)').text.strip()
            c = pp.select_one('td:nth-child(4)').text.strip()
            d = pp.select_one('td:nth-child(5)').text.strip()
            e = pp.select_one('td:nth-child(6)').text.strip()
            f = pp.select_one('td:nth-child(7)').text.strip()

            doc = {
                'z': z,
                'year': y,
                'asset': a,
                'bond': b,
                'equity': c,
                'revenue': d,
                'ebit': e,
                'ni': f,
            }
            db.fc_fs.insert_one(doc)
        except:
            pass

    title = soup.select('#frm > div:nth-child(12) > div > table:nth-child(5) > tbody > tr:nth-child(3)')
    for pp in title:
        try:
            y = pp.select_one('td.noborder').text.strip()
            a = pp.select_one('td:nth-child(2)').text.strip()
            b = pp.select_one('td:nth-child(3)').text.strip()
            c = pp.select_one('td:nth-child(4)').text.strip()
            d = pp.select_one('td:nth-child(5)').text.strip()
            e = pp.select_one('td:nth-child(6)').text.strip()
            f = pp.select_one('td:nth-child(7)').text.strip()

            doc = {
                'z': z,
                'year': y,
                'asset': a,
                'bond': b,
                'equity': c,
                'revenue': d,
                'ebit': e,
                'ni': f,
            }
            db.fc_fs.insert_one(doc)
        except:
            pass

    title = soup.select('#frm > div:nth-child(12) > div > table:nth-child(5) > tbody > tr:nth-child(4)')
    for pp in title:
        try:
            y = pp.select_one('td.noborder').text.strip()
            a = pp.select_one('td:nth-child(2)').text.strip()
            b = pp.select_one('td:nth-child(3)').text.strip()
            c = pp.select_one('td:nth-child(4)').text.strip()
            d = pp.select_one('td:nth-child(5)').text.strip()
            e = pp.select_one('td:nth-child(6)').text.strip()
            f = pp.select_one('td:nth-child(7)').text.strip()

            doc = {
                'z': z,
                'year': y,
                'asset': a,
                'bond': b,
                'equity': c,
                'revenue': d,
                'ebit': e,
                'ni': f,
            }
            db.fc_fs.insert_one(doc)
        except:
            pass
