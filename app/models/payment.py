from app import db
from flask import abort, make_response, jsonify


class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    last_four = db.Column(db.String)
    link = db.Column(db.String)
    survey = db.relationship("Survey", back_populates="payment")

    @classmethod
    def from_dict(cls, payment_data):
        try:
            new_survey = cls(
                last_four=payment_data["last_four"],
                link=payment_data["link"],
            )

        except KeyError:
            abort(make_response(jsonify({"details": "Invalid data"}), 400))

        return new_survey

    def to_dict(self):
        payment_dict = {}
        payment_dict["id"] = self.payment_id
        payment_dict["last_four"] = self.last_four
        payment_dict["link"] = self.link

        return payment_dict

    def update_from_dict(self, payment_data):
        for k, v in payment_data.items():
            if hasattr(self, k):
                setattr(self, k, v)
