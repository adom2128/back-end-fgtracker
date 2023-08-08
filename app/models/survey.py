from app import db
from datetime import datetime, timezone
from flask import abort, make_response, jsonify


class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.String(255), nullable=True)
    date_survey_completed = db.Column(db.DateTime)
    payment = db.Column(db.Numeric(), nullable=False, default=0)
    stage = db.Column(db.String(100), nullable=False)
    date_fg_completed = db.Column(db.DateTime, default=None)
    payment_received = db.Column(db.Boolean, nullable=False, default=False)
    payment_expiration_date = db.Column(db.DateTime, default=None)
    payment_left = db.Column(db.Numeric(), default=0)
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.payment_id'), nullable=False)
    payment = db.relationship("Payment", back_populates="survey")

    @classmethod
    def from_dict(cls, survey_data):
        try:
            new_survey = cls(
                company=survey_data["company"],
                topic=survey_data["topic"],
                notes=survey_data.get("notes", None),
                date_survey_completed=survey_data.get(
                    "date_survey_completed", datetime.now(timezone.utc)
                ),
                payment=survey_data.get("payment", 0),
                stage=survey_data.get("stage", "Applied"),
                date_fg_completed=survey_data.get("date_fg_completed", None),
                payment_received=survey_data.get("payment_received", False),
                payment_expiration_date=survey_data.get(
                    "payment_expiration_date", None
                ),
                payment_left=survey_data.get("payment_left", 0),
            )

            if survey_data.get("date_fg_completed"):
                new_survey.date_fg_completed = datetime.strptime(
                    survey_data["date_fg_completed"], "%Y-%m-%d"
                )

            if survey_data.get("payment_expiration_date"):
                new_survey.payment_expiration_date = datetime.strptime(
                    survey_data["payment_expiration_date"], "%Y-%m-%d"
                )

        except KeyError:
            abort(make_response(jsonify({"details": "Invalid data"}), 400))

        return new_survey

    def to_dict(self):
        survey_dict = {}
        survey_dict["id"] = self.id
        survey_dict["company"] = self.company
        survey_dict["topic"] = self.topic
        survey_dict["notes"] = self.notes
        survey_dict["date_survey_completed"] = self.date_survey_completed
        survey_dict["payment"] = float(self.payment)
        survey_dict["stage"] = self.stage
        survey_dict["date_fg_completed"] = self.date_fg_completed
        survey_dict["payment_received"] = self.payment_received
        survey_dict["payment_expiration_date"] = self.payment_expiration_date
        survey_dict["payment_left"] = float(self.payment_left)

        return survey_dict

    def update_from_dict(self, survey_data):
        for k, v in survey_data.items():
            if hasattr(self, k):
                setattr(self, k, v)

        if survey_data.get("date_fg_completed"):
            self.date_fg_completed = datetime.strptime(
                survey_data["date_fg_completed"], "%Y-%m-%d"
            )

        if survey_data.get("payment_expiration_date"):
            self.payment_expiration_date = datetime.strptime(
                survey_data["payment_expiration_date"], "%Y-%m-%d"
            )
