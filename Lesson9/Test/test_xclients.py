import pytest
from Lesson9.Pages.Employee import Employeer
from Lesson9.Pages.DataBase import DataBase

api = Employeer("https://x-clients-be.onrender.com")
db = DataBase(
    "postgresql+psycopg2://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

def test_get_list_of_employers():
    db.create_company('Verochka', 'my_company')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Vera", "Popova", "Ivanovna", "8005553535")
    db_employer_list = db.get_list_employer(max_id)
    
    assert db_employer_list is not None, "DB employer list is None"
    assert len(db_employer_list) > 0, "DB employer list is empty"
    
    api_employer_list = api.get_list(max_id)
    
    assert api_employer_list is not None, "API employer list is None"
    assert len(api_employer_list) > 0, "API employer list is empty"
    
    assert len(db_employer_list) == len(api_employer_list)
    
    response = api_employer_list[0]
    employer_id = response['id']
    db.delete_employer(employer_id)
    db.delete_company(max_id)