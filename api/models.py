from . import db

class WeathModel(db.Model):
    __tablename__ = 'weathers'
    id = db.Column(db.Integer(), primary_key=True)
    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())
    temperature = db.Column(db.Integer())
    timess = db.Column(db.DateTime(), index=True)
    date_del = db.Column(db.DateTime(), index=True)

    def __str__(self):
        return f'{self.id}'
