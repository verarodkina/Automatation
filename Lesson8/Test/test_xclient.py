import pytest
import requests
import _json
from Lesson8.Pages.Employee import Employeer, Company
from Lesson8.constants import x_client_url

employeer = Employeer()
company = Company()

def test_authorization(get_token):
    token = get_token
    assert token is not None
    assert isinstance(token, str)

def test_getcompany_id():
    company_id = company.last_active_company_id()
    assert company_id is not None
    assert str(company_id).isdigit()

def test_add_employer(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
        'id':0,
        'firstName': 'Ivan',
        'lastName': 'Petrov',
        'middleName': 'string',
        'companyID': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-05-16T11:02:45.622Z',
        'isActive': 'true'
    }
    new_employer_id = (employeer.add_new(token, body_employer))['id']
    assert new_employer_id is not None
    assert str (new_employer_id).isdigit()

    info = employeer.get_info(new_employer_id)
    assert info.json()['id'] == new_employer_id
    assert info.status_code == 200

    def test_add_employer_without_token():
        com_id = company.last_active_company_id()
        token = ""
        body_employer = {'id':0,
        'firstName': 'Ivan',
        'lastName': 'Petrov',
        'middleName': 'string',
        'companyID': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-05-16T11:02:45.622Z',
        'isActive': 'true'
        }
        new_employer = employeer.add_new(token, body_employer)
        assert new_employer['message'] == 'Unauthorized'

    def test_add_employer_without_body(get_token):
        token = str(get_token)
        com_id = company.last_active_company_id()
        body_employer = {}
        new_employer = employeer.add_new(token, body_employer)
        assert new_employer['message'] == 'Internal server error'

    def test_get_employer():
        com_id = company.last_active_company_id()
        list_employers = employeer.get_list(com_id)
        assert isinstance(list_employers, list)


    def test_get_list_employers_missing_company_id():
        try:
            employeer.get_list()
        except TypeError as e:
            assert str(
                e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"
            
    def test_get_list_employers_invalid_company_id():
        try:
            employeer.get_list('')
        except TypeError as e:
            assert str(
                e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"
            

    def test_change_employer_info(get_token):
        token = str(get_token)
        com_id = company.last_active_company_id()
        body_employer = {'id':0,
        'firstName': 'Ivan',
        'lastName': 'Petrov',
        'middleName': 'string',
        'companyID': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-05-16T11:02:45.622Z',
        'isActive': 'true'
        }
        just_employer = employeer.add_new(token, body_employer)
        id = just_employer['id']
        body_change_employer = {
        'lastName': 'Vasiliev',
        'email': 'testtt@mail.ru',
        'url': 'string',
        'phone': 'string',
        'isActive': 'true'
        }
        employer_changed = employeer.change_info(token, id, body_change_employer)
        assert employer_changed.status_code == 200
        assert id == employer_changed.json()['id']
        assert(employer_changed.json()["email"]) == body_change_employer.get("email")   





    

