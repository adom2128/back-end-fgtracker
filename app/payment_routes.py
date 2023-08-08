from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.payment import Payment
from .route_helpers import validate_model
from sqlalchemy import desc

payments_bp = Blueprint("payment", __name__, url_prefix="/payments")


@payments_bp.route("", methods=["GET"])
def get_all_payments():
    payments_query = Payment.query.all()

    payments_response = [payment.to_dict() for payment in payments_query]

    return make_response(jsonify(payments_response), 200)


@payments_bp.route("", methods=["POST"])
def create_payment():
    request_body = request.get_json()

    new_payment = Payment.from_dict(request_body)

    db.session.add(new_payment)
    db.session.commit()

    return jsonify(new_payment.to_dict()), 201

@payments_bp.route("/<payment_id>", methods=["PUT"])
def update_payment(payment_id):
    updated_payment = validate_model(Payment, payment_id)

    request_body = request.get_json()
    updated_payment.update_from_dict(request_body)

    db.session.commit()

    return jsonify(updated_payment.to_dict()), 200


@payments_bp.route("/<payment_id>", methods=["DELETE"])
def delete_payment(payment_id):
    payment_to_delete = validate_model(Payment, payment_id)

    db.session.delete(payment_to_delete)
    db.session.commit()

    return make_response(
        jsonify({"details": f"payment {payment_id} successfully deleted"}), 200
    )