


from config import db


Base = db.declarative_base()

class Property(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String, nullable=False)
    seller = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    