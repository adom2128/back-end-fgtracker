from app.models.survey import Survey
import pytest
from datetime import date


def test_get_surveys_no_saved_surveys(client):
    response = client.get("/surveys")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


def test_get_surveys_one_saved(client, one_survey):
    response = client.get("/surveys")
    response_body = response.get_json()

    assert response.status_code == 200

    json_date_str = response_body[0]["date_completed"]
    today_date_str = date.today().strftime("%a, %d %b %Y %H:%M:%S %Z") + "GMT"
    assert json_date_str == today_date_str

    assert response_body == [
        {
            "company": "Fieldwork Denver",
            "date_completed": today_date_str,
            "notes": None,
            "payment": 150.0,
            "payment_expiration_date": None,
            "payment_left": 0.0,
            "payment_received": False,
            "stage": "Applied",
            "survey_id": 1,
            "topic": "TV Shows",
        }
    ]


def test_get_surveys_three_saved(client, three_surveys):
    response = client.get("/surveys")
    response_body = response.get_json()

    assert response.status_code == 200

    json_date_str_one = response_body[0]["date_completed"]
    json_date_str_two = response_body[1]["date_completed"]
    json_date_str_three = response_body[2]["date_completed"]
    today_date_str = date.today().strftime("%a, %d %b %Y %H:%M:%S %Z") + "GMT"
    assert json_date_str_one == today_date_str
    assert json_date_str_two == today_date_str
    assert json_date_str_three == today_date_str

    assert response_body == [
        {
            "company": "Fieldwork Denver",
            "date_completed": today_date_str,
            "notes": None,
            "payment": 150.0,
            "payment_expiration_date": None,
            "payment_left": 0.0,
            "payment_received": False,
            "stage": "Applied",
            "survey_id": 1,
            "topic": "TV Shows",
        },
        {
            "company": "Opinions for Cash",
            "date_completed": today_date_str,
            "notes": None,
            "payment": 125.0,
            "payment_expiration_date": None,
            "payment_left": 0.0,
            "payment_received": False,
            "stage": "Applied",
            "survey_id": 2,
            "topic": "Vitamins for Hispanics",
        },
        {
            "company": "Ascendancy Research",
            "date_completed": today_date_str,
            "notes": None,
            "payment": 140.0,
            "payment_expiration_date": None,
            "payment_left": 0.0,
            "payment_received": False,
            "stage": "Applied",
            "survey_id": 3,
            "topic": "Job Searching",
        },
    ]


def test_create_survey_with_limited_information(client):
    response = client.post(
        "/surveys",
        json={"company": "Fieldwork Denver", "topic": "TV Shows", "payment": 150},
    )
    response_body = response.get_json()

    assert response.status_code == 201
    json_date_str = response_body["date_completed"]
    today_date_str = date.today().strftime("%a, %d %b %Y %H:%M:%S %Z") + "GMT"
    assert json_date_str == today_date_str

    assert response_body == {
        "company": "Fieldwork Denver",
        "date_completed": today_date_str,
        "notes": None,
        "payment": 150.0,
        "payment_expiration_date": None,
        "payment_left": 0.0,
        "payment_received": False,
        "stage": "Applied",
        "survey_id": 1,
        "topic": "TV Shows",
    }

    new_survey = Survey.query.get(1)
    assert new_survey
    assert new_survey.company == "Fieldwork Denver"
    assert new_survey.topic == "TV Shows"
    assert new_survey.payment == 150
    assert new_survey.stage == "Applied"
    assert new_survey.payment_received == False
    assert new_survey.notes == None


def test_create_survey_with_all_information(client):
    response = client.post(
        "/surveys",
        json={
            "company": "Fieldwork Denver",
            "topic": "TV Shows",
            "payment": 150,
            "notes": "job as program manager",
            "stage": "Applied",
            "payment_received": False,
            "payment_expiration_date": None,
            "payment_left": 0,
            "payment_received": 0,
        },
    )
    response_body = response.get_json()

    assert response.status_code == 201
    json_date_str = response_body["date_completed"]
    today_date_str = date.today().strftime("%a, %d %b %Y %H:%M:%S %Z") + "GMT"
    assert json_date_str == today_date_str

    assert response_body == {
        "company": "Fieldwork Denver",
        "date_completed": today_date_str,
        "notes": "job as program manager",
        "payment": 150.0,
        "payment_expiration_date": None,
        "payment_left": 0.0,
        "payment_received": False,
        "stage": "Applied",
        "survey_id": 1,
        "topic": "TV Shows",
    }

    new_survey = Survey.query.get(1)
    assert new_survey
    assert new_survey.company == "Fieldwork Denver"
    assert new_survey.topic == "TV Shows"
    assert new_survey.payment == 150
    assert new_survey.stage == "Applied"
    assert new_survey.payment_received == False
    assert new_survey.notes == "job as program manager"


def test_create_survey_no_company(client):
    response = client.post("/surveys", json={"topic": "TV Shows", "payment": 150})
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"details": "Invalid data"}
    assert Survey.query.all() == []


def test_create_survey_no_topic(client):
    response = client.post(
        "/surveys", json={"company": "Fieldwork Denver", "payment": 150}
    )
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"details": "Invalid data"}
    assert Survey.query.all() == []


def test_update_survey(client, one_survey):
    response = client.put(
        "/surveys/1", json={"payment_received": True, "payment_left": 75}
    )
    response_body = response.get_json()

    assert response.status_code == 200

    json_date_str = response_body["date_completed"]
    today_date_str = date.today().strftime("%a, %d %b %Y %H:%M:%S %Z") + "GMT"
    assert json_date_str == today_date_str

    assert response_body == {
        "company": "Fieldwork Denver",
        "date_completed": today_date_str,
        "notes": None,
        "payment": 150.0,
        "payment_expiration_date": None,
        "payment_left": 75.0,
        "payment_received": True,
        "stage": "Applied",
        "survey_id": 1,
        "topic": "TV Shows",
    }

    survey = Survey.query.get(1)
    assert survey.payment_received == True
    assert survey.payment_left == 75


def test_update_survey_not_found(client):
    response = client.put(
        "/surveys/1", json={"payment_received": True, "payment_left": 75}
    )
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message": "Survey 1 not found"}


def test_delete_survey(client, one_survey):
    response = client.delete("/surveys/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"details": "Survey 1 successfully deleted"}
    assert Survey.query.get(1) == None


def test_delete_survey_not_found(client):
    response = client.delete("/surveys/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Survey 1 not found"}
    assert Survey.query.all() == []


def test_delete_multiple_surveys(client, three_surveys):
    response = client.delete("/surveys/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {"details": "Survey 1 successfully deleted"}
    assert len(Survey.query.all()) == 2
