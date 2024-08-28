import pytest
from Lesson9.Pages.Employee import Employeer
from Lesson9.Pages.DataBase import DataBase

api = Employeer("https://x-clients-be.onrender.com")
db = DataBase(
    "postgresql+psycopg2://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

def test_get_list_of_employers():
    db.create_company('Verochka', 'my_company')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Vera", "Popova", 8005553535)
    db_employer_list = db.get_list_employer(max_id)
    api_employer_list = api.get_list(max_id)
    assert len(db_employer_list) == len(api_employer_list)
    responce = (api.get_list(max_id))[0]
    employer_id = responce['id']
    db.delete_employer(employer_id)
    db.delete(max_id)

def test_add_new_eployer():
    db.create_company('Vera adding new employer', 'employer')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Vera", "Popova", 800555353500)
    responce = (api.get_list(max_id))[0]
    employer_id = responce["id"]
    assert responce[companyID] == max_id
    assert responce ["firstName"] == "Vera"
    assert responce ["isActive"] == True
    assert responce ["lastName"] == "Popova"
    db.delete_employer(employer_id)
    db.delete(max_id)


def test_assertion_data():
    db.create_company('Employer get id company', 'new')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Vera", "Popova", 800555353500)
    employer_id = db.get_employer_id(max_id)
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info ["firstName"] == "Vera"
    assert get_api_info ["lastName"] == "Popova"
    assert get_api_info ["isActive"] == True
    db.delete_employer(employer_id)
    db.delete(max_id)

