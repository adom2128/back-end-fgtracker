from app import db
from datetime import date
from flask import abort, make_response, jsonify


class Survey(db.Model):
    survey_id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.String(255), nullable=True)
    date_completed = db.Column(db.Date, nullable=False)
    compensation = db.Column(db.Numeric(), nullable=False)
    stage = db.Column(db.String(100), nullable=False)
    payment_received = db.Column(db.Boolean, nullable=False)
    payment_expiration_date = db.Column(db.Date, default=None)
    payment_left = db.Column(db.Numeric(), default=0)

    @classmethod
    def from_dict(cls, survey_data):
        try:
            new_survey = cls(
                company=survey_data["company"],
                topic=survey_data["topic"],
                notes=survey_data.get("notes", None),
                date_completed=date.today(),
                compensation=survey_data.get("compensation", 0),
                stage=survey_data.get("stage", "Applied"),
                payment_received=survey_data.get("payment_received", False),
                payment_expiration_date=survey_data.get(
                    "payment_expiration_date", None
                ),
                payment_left=survey_data.get("payment_left", 0),
            )
        except KeyError:
            abort(make_response(jsonify({"details": "Invalid data"}), 400))

        return new_survey

    def to_dict(self):
        survey_dict = {}
        survey_dict["survey_id"] = self.survey_id
        survey_dict["company"] = self.company
        survey_dict["topic"] = self.topic
        survey_dict["notes"] = self.notes
        survey_dict["date_completed"] = self.date_completed
        survey_dict["compensation"] = float(self.compensation)
        survey_dict["stage"] = self.stage
        survey_dict["payment_received"] = float(self.payment_received)
        survey_dict["payment_expiration_date"] = self.payment_expiration_date
        survey_dict["payment_left"] = float(self.payment_left)

        return survey_dict
