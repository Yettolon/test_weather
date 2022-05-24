# test_weather
flask

# Установка

git init

git clone https://github.com/Yettolon/test_weather.git

python3 -m venv venv

source venv/bin/activate

cd test_weather

pip install -r requirements.txt

export FLASK_APP=api

export FLASK_ENV=development

flask db init

flask db migrate

flask db upgrade

flask run


# Создание записей.(Желательно добавить больше 2000).

python3 local_post.py

Получение массива с случайными фильтрами.

python3 local_get.py