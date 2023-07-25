from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.survey import Survey
from .route_helpers import validate_model

surveys_bp = Blueprint("survey", __name__, url_prefix="/surveys")


@surveys_bp.route("", methods=["GET"])
def get_all_surveys():
    surveys = Survey.query.all()

    surveys_response = [survey.to_dict() for survey in surveys]

    return make_response(jsonify(surveys_response), 200)


@surveys_bp.route("", methods=["POST"])
def create_survey():
    request_body = request.get_json()

    new_survey = Survey.from_dict(request_body)

    db.session.add(new_survey)
    db.session.commit()

    return jsonify(new_survey.to_dict()), 200


@surveys_bp.route("/<survey_id>", methods=["PUT"])
def update_survey(survey_id):
    updated_survey = validate_model(Survey, survey_id)

    request_body = request.get_json()
    updated_survey.update_from_dict(request_body)

    db.session.commit()

    return jsonify(updated_survey.to_dict()), 200
