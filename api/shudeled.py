
import os

import sqlalchemy
from datetime import datetime, date, timedelta
from sqlalchemy import create_engine

def sheduled_task():
    engine =  create_engine('postgresql://admin:admin@localhost/weather_db')
    todays_datetime = datetime(datetime.today().year, datetime.today().month,
                    datetime.today().day, datetime.today().hour,
                    datetime.today().minute, datetime.today().second)
    #getting data
    q = "DELETE FROM weathers WHERE date_del < :todays_datetime"
    engine.execute(sqlalchemy.text(q), {'todays_datetime': todays_datetime})


def shudeled_task_records():
    date_now = date.today()
    date_del = (date_now - timedelta(days=5)).strftime('%Y-%m-%d')
    path_file = os.path.abspath("record.log")
    lines = None
    with open(path_file, "r") as f:
        lines = f.readlines()
    with open(path_file, "w") as f:
        for i in lines:
            if i[:10]!=date_del and i[:4].isdigit():
                    f.write(i)



