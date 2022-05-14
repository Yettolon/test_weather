from itertools import count
import requests
import pytz
from datetime import datetime
import random

def get_number():
    while True:
        getNumber = input('Введите целое положительное число: ')

        if getNumber.isdigit() : return int(getNumber)

counts = get_number()

tz = pytz.timezone('Africa/Timbuktu')
date_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
for i in range(counts):
    requests.post('http://80.249.146.142/', json={'lat':round(random.uniform(-90.00,90.00),2),'lng':round(random.uniform(-180.00,180.00),2),'temperature':random.randint(-100,100),'time':date_time})

