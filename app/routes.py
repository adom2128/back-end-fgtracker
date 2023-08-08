from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.survey import Survey
from .route_helpers import validate_model
from sqlalchemy import desc

surveys_bp = Blueprint("survey", __name__, url_prefix="/surveys")


@surveys_bp.route("", methods=["GET"])
def get_all_surveys():
    query = Survey.query

    survey_query = query.order_by(desc(Survey.date_survey_completed))

    surveys_response = [survey.to_dict() for survey in survey_query]

    return make_response(jsonify(surveys_response), 200)


@surveys_bp.route("", methods=["POST"])
def create_survey():
    request_body = request.get_json()

    new_survey = Survey.from_dict(request_body)

    db.session.add(new_survey)
    db.session.commit()

    return jsonify(new_survey.to_dict()), 201


@surveys_bp.route("/<survey_id>", methods=["PUT"])
def update_survey(survey_id):
    updated_survey = validate_model(Survey, survey_id)

    request_body = request.get_json()
    updated_survey.updated_survey.update_from_dict(request_body)

    db.session.commit()

    return jsonify(updated_survey.to_dict()), 200


@surveys_bp.route("/<survey_id>", methods=["DELETE"])
def delete_survey(survey_id):
    survey_to_delete = validate_model(Survey, survey_id)

    db.session.delete(survey_to_delete)
    db.session.commit()

    return make_response(
        jsonify({"details": f"Survey {survey_id} successfully deleted"}), 200
    )


@surveys_bp.route("/<survey_id>", methods=["PATCH"])
def update_payment_balance(survey_id):
    survey = validate_model(Survey, survey_id)

    request_body = request.get_json()
    survey.update_from_dict(request_body)
    
    db.session.commit()

    return jsonify(survey.to_dict()), 200
