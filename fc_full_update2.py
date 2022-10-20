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

    # fee
    title = soup.select('#frm > div:nth-child(15) > div > table:nth-child(2) > tbody > tr')
    for pp in title:
        try:
            i = pp.select_one('td.noborder').text.strip()
            a = pp.select_one('td:nth-child(2)').text.strip()
            b = pp.select_one('td:nth-child(3)').text.strip()
            c = pp.select_one('td:nth-child(4)').text.strip()
            d = pp.select_one('td:nth-child(5)').text.strip()

            doc = {
                'z': z,
                'i': i,
                'a': a,
                'b': b,
                'c': c,
                'd': d,
            }
            db.fc_fee.insert_one(doc)
        except:
            pass

    # interior
    title = soup.select('#frm > div:nth-child(15) > div > table:nth-child(4) > tbody > tr')
    for pp in title:
        try:
            i = pp.select_one('td.noborder').text.strip()
            a = pp.select_one('td:nth-child(2)').text.strip()
            b = pp.select_one('td:nth-child(3)').text.strip()
            doc = {
                'z': z,
                'i': i,
                'a': a,
                'b': b,
            }
            db.fc_interior.insert_one(doc)
        except:
            pass

    # contract
    title = soup.select('#frm > div:nth-child(16) > div > table')
    for pp in title:
        try:
            a = pp.select_one('td.noborder').text.strip()
            b = pp.select_one('td:nth-child(2)').text.strip()
            doc = {
                'z': z,
                'a': a,
                'b': b,
            }
            db.fc_contract.insert_one(doc)
        except:
            pass

    # correction
    title = soup.select('#frm > div:nth-child(14) > div > table > tbody > tr')
    for pp in title:
        try:
            i = pp.select_one('td.noborder').text.strip()
            a = pp.select_one('td:nth-child(2)').text.strip()
            b = pp.select_one('td:nth-child(3)').text.strip()
            doc = {
                'z': z,
                'i': i,
                'a': a,
                'b': b,
            }
            db.fc_correction.insert_one(doc)
        except:
            pass

    # deposit
    title = soup.select('#frm > div:nth-child(13) > div > table:nth-child(14) > tbody')
    for pp in title:
        try:
            i = pp.select_one('tr:nth-child(1) > td').text.strip()
            a = pp.select_one('tr:nth-child(2) > td').text.strip()
            doc = {
                'z': z,
                'i': i,
                'a': a,
            }
            db.fc_deposit.insert_one(doc)
        except:
            pass

    # ad_cost
    title = soup.select('#frm > div:nth-child(13) > div > table:nth-child(12) > tbody > tr')

    for pp in title:
        try:
            i = pp.select_one('td.noborder').text.strip()
            a = pp.select_one('td:nth-child(2)').text.strip()
            b = pp.select_one('td:nth-child(3)').text.strip()

            doc = {
                'z': z,
                'i': i,
                'a': a,
                'b': b,
            }
            db.fc_ad_cost.insert_one(doc)
        except:
            pass

    # region_num
    title = soup.select('#frm > div:nth-child(13) > div > table:nth-child(10) > tbody > tr')
    for pp in title:
        try:
            i = pp.select_one('td').text.strip()

            doc = {
                'z': z,
                'region_count': i,
            }
            db.fc_region_count.insert_one(doc)
        except:
            pass

    # openday
    title = soup.select('#frm > div:nth-child(13) > div > table:nth-child(2) > tbody > tr')
    for pp in title:
        try:
            i = pp.select_one('td').text.strip()

            doc = {
                'z': z,
                'openday': i,
            }
            db.fc_openday.insert_one(doc)
        except:
            pass

    # brand_num
    title = soup.select('#frm > div:nth-child(12) > div > table:nth-child(9) > tbody > tr')
    for pp in title:
        try:
            i = pp.select_one('td.noborder').text.strip()
            a = pp.select_one('td:nth-child(2)').text.strip()
            doc = {
                'z': z,
                'brand_num': i,
                'family_num': a,
            }
            db.fc_brand_count.insert_one(doc)
        except:
            pass

    # staff
    title = soup.select('#frm > div:nth-child(12) > div > table:nth-child(7)')
    for pp in title:
        try:
            i = pp.select_one('td.noborder').text.strip()
            a = pp.select_one('td:nth-child(2)').text.strip()
            b = pp.select_one('td:nth-child(3)').text.strip()

            doc = {
                'z': z,
                'year': i,
                'manager_num': a,
                'staff_num': b,
            }
            db.fc_staff.insert_one(doc)
        except:
            pass

    # class
    title = soup.select('#frm > div:nth-child(12) > div > table:nth-child(3) > tbody > tr:nth-child(2)')
    for pp in title:
        try:
            i = pp.select_one('td:nth-child(2)').text.strip()
            a = pp.select_one('td:nth-child(4)').text.strip()
            b = pp.select_one('td:nth-child(6)').text.strip()

            doc = {
                'z': z,
                'biz_type': i,
                'corp_no': a,
                'biz_no': b,
            }
            db.fc_class.insert_one(doc)
        except:
            pass

    # address
    title = soup.select('#frm > div:nth-child(12) > div > table:nth-child(3) > tbody > tr:nth-child(1)')
    for pp in title:
        try:
            i = pp.select_one('td').text.strip()
            doc = {
                'z': z,
                'address': i,
            }
            db.fc_address.insert_one(doc)
        except:
            pass
