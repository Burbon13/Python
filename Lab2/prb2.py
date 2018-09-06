from datetime import date
import datetime

ziua = int(input())
luna = int(input())
anul = int(input())

d0 = date(anul,luna,ziua)
d1 = date(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day)

print((d1-d0).days//365);



