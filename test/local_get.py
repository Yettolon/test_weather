import requests
import random

res = requests.get(
    f"http://127.0.0.1:5000/?lat={round(random.uniform(-90.00,90.00),2)}&lng={round(random.uniform(-90.00,90.00),2)}&radius={random.randint(0,500)}"
)

print(res.json())
