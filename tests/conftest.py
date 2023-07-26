import pytest
from app import create_app
from app import db
from app.models.survey import Survey


@pytest.fixture
def app():
    # create the app with a test config dictionary
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    # close and remove the temporary database
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def one_survey(app):
    new_survey = Survey(company="Fieldwork Denver", topic="TV Shows", payment=150)
    db.session.add(new_survey)
    db.session.commit()


@pytest.fixture
def three_surveys(app):
    db.session.add_all(
        [
            Survey(company="Fieldwork Denver", topic="TV Shows", payment=150),
            Survey(
                company="Opinions for Cash", topic="Vitamins for Hispanics", payment=125
            ),
            Survey(company="Ascendancy Research", topic="Job Searching", payment=140),
        ]
    )
    db.session.commit()
