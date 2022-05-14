import requests
import random

res = requests.get(f'http://80.249.146.142/?lat={round(random.uniform(-90.00,90.00),2)}&lng={round(random.uniform(-90.00,90.00),2)}&radius={random.randint(0,500)}')

print(res.json())
