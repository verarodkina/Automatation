import json
import requests
import allure
from Homework.Test.conftest import x_client_url

path = '/employee'

class Company:
    def __init__(self,url=x_client_url):
        self.url = url

        
    def create(self, token: str, body: json):
        headers = {'x-client-token':token}
        responce = requests.post(
            self.url + '/company', headers=headers, params=body)
        return responce.json()
    
    def last_active_company_id(self):
        active_params = {'active':'true'}
        responce = requests.get(
            self.url + '/company', params=active_params)
        return responce.json()[-1]['id']
    
class Employeer:
    def __init__(self, url=x_client_url):
        self.url = url

    @allure.step("Получить список сотрудников по id компании")
    def get_list (self, company_id:int):
        company = {'company':company_id}
        responce = requests.get(
            self.url + '/employee', params=company)
        return responce.json()
    
    @allure.step("Добавить сотрудникав компанию")
    def add_new(self, token: str, body: json):
        headers = {'x-client-token':token}
        responce = requests.post(
            self.url + '/employee', headers=headers, json=body) 
        return responce.json()
    
    @allure.step("Получаем информацию о сотруднике по ID")
    def get_info(self, employee_id: int):
        responce = requests.get(self.url + path + str(employee_id))
        return responce
    
    @allure.step("Обновляем данные о сотруднике")
    def change_info(self, token:str, employee_id:int, body:json):
        headers = {'x-client-token':token}
        responce = requests.patch(self.url + path + str(employee_id), headers=headers,
                                  json=body)
        return responce
        