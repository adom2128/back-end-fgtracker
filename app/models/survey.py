from app import db


class Survey(db.Model):
    survey_id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.String(255), nullable=True)
    date_completed = db.Column(db.Date, nullable=False)
    compensation = db.Column(db.Numeric(4, 2), nullable=False, default=0)
    stage = db.Column(db.String(100), nullable=False, default="Applied")
    payment_received = db.Column(db.Boolean, nullable=False, default=False)
    payment_expiration_date = db.Column(db.Date, default=None)
    payment_left = db.Column(db.Numeric(4, 2), default=0)
