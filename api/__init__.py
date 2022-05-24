import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_apscheduler import APScheduler

from config import Config
from .shudeled import shudeled_task_records, sheduled_task


db = SQLAlchemy()
migrate = Migrate()
scheduler = APScheduler()


app = Flask(__name__)
app.config.from_object(Config)
app.debug = True

# logging
logging.basicConfig(
    filename="record.log",
    level=logging.INFO,
    format=f"%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)
logging.getLogger("apscheduler.executors.default").propagate = False

db.init_app(app)
migrate.init_app(app, db)

from .api import api as api_blueprint

app.register_blueprint(api_blueprint, url_prefix="/")


scheduler.add_job(
    id="Scheduled task",
    func=sheduled_task,
    trigger="interval",
    seconds=120,
    misfire_grace_time=9999999999999,
)
scheduler.add_job(
    id="Scheduled task 2",
    func=shudeled_task_records,
    trigger="interval",
    seconds=360,
    misfire_grace_time=9999999999999,
)

scheduler.start()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
