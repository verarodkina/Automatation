import pytest
import allure
from Homework.Pages.Employee import Employeer
from Homework.Pages.DataBase import DataBase

api = Employeer("https://x-clients-be.onrender.com")
db = DataBase(
    "postgresql+psycopg2://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")


@allure.epic("x-clients")
@allure.severity(severity_level='normal')
@allure.title("Список сотрудников")
@allure.description("Получить список список сотрудников из БД и API, сравнить их")
@allure.feature('Тест 1')

def test_get_list_of_employers():
    with allure.step("Сздание компании"):
        db.create_company('Verochka', 'my_company')
    with allure.step("Получить ID последней компании"):    
        max_id = db.last_company_id()
    with allure.step("Добавить сотрудника в компанию"):    
        db.create_employer(max_id, "Vera", "Popova", 8005553535)
    with allure.step("Получить список сотрудников из последней компании"):    
        db_employer_list = db.get_list_employer(max_id)
    with allure.step("api-получить список сотрудников из последней компании"):    
        api_employer_list = api.get_list(max_id)
    with allure.step("Сравнить списки БД и API"):
        assert len(db_employer_list) == len(api_employer_list)
    with allure.step("Удалить созданного сотрудника"):    
        response = (api.get_list(max_id))[0]
        employer_id = response["id"]
        db.delete_employer(employer_id)
    with allure.step("Удалить последнюю компанию"):    
        db.delete(max_id)

@allure.epic("x-clients")
@allure.severity(severity_level='critical')
@allure.title("Добавление сотрудников")
@allure.description("Добавить сотрудника в БД и сравнить с API")
@allure.feature('Тест 2')

def test_add_new_employer():
    with allure.step("Добавить сотрудника"):
        db.create_company('Vera adding new employer', 'employer')
    with allure.step("Получить ID последней компании"):    
        max_id = db.last_company_id()
    with allure.step("Добавить сотрудника в компанию"):    
        db.create_employer(max_id, "Vera", "Popova", 800555353500)
        response = (api.get_list(max_id))[0]
        employer_id = response["id"]
    with allure.step("Сравнить ID компании"):    
        assert response["companyId"] == max_id
    with allure.step("Сравнить имя"):    
        assert response["firstName"] == "Vera"
    with allure.step("Сравнить статус"):    
        assert response["isActive"] == True
    with allure.step("Сравнить фамилию"):    
        assert response["lastName"] == "Popova"
    with allure.step("Удалить созданного сотрудника"):    
        db.delete_employer(employer_id)
    with allure.step("Удалить последнюю компанию"):    
        db.delete(max_id)


