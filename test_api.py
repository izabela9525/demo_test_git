import pytest
import requests
import uuid

@pytest.mark.Registration
def test_registration():
    APIURL = f'https://test.manulo.sagiton.pl:/api/v1/company/register'
    response = requests.post(
        APIURL,
        json = {
            "companyName": "Sebke63465456",
            "email": "sebek34564652@yopmail.com",
            "firstName": f"Seba{uuid.uuid4()}",
            "lastName": f"Test{uuid.uuid4()}",
            "password": "Test1234",
            "subscriptionPlan": "TRIAL",
            "username": "Seba"
            },
        headers = {
            'Content-Type': 'application/json'}
    )
    assert response.status_code == 200

