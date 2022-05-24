import requests
import datetime
import random


def get_number():
    while True:
        getNumber = input("Введите целое положительное число: ")

        if getNumber.isdigit():
            return int(getNumber)


counts = get_number()

date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

for i in range(counts):
    requests.post(
        "http://127.0.0.1:5000/",
        json={
            "lat": round(random.uniform(-90.00, 90.00), 2),
            "lng": round(random.uniform(-180.00, 180.00), 2),
            "temperature": random.randint(0, 100),
            "time": date_time,
        },
    )
