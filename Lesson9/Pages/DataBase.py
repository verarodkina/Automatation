from sqlalchemy import create_engine, text
import psycopg2

class DataBase:
    query = {
        'create_company': text('INSERT INTO company(name, description) VALUES(:name, :description)'),
        'max_company_id': text('SELECT MAX(id) FROM company'),
        'delete_company': text('DELETE FROM company WHERE id = :company_id'),
        'list_SELECT': text('SELECT * FROM employee WHERE company_id = :id'),
        'item_SELECT':  text('SELECT * FROM employee WHERE company_id = :c_id AND id = :e_id'),
        'maxID_SELECT':  text('SELECT MAX(id) FROM employee WHERE company_id = :c_id'), 
        'item_DELETE':  text('DELETE FROM employee WHERE id = :id_delete'),
        'item_UPDATE':  text('UPDATE employee SET first_name = :new_name WHERE id = :employer_id'),
        'item_INSERT':  text('INSERT INTO employee(company_id, first_name, last_name, middle_name, phone, email, avatar_url) '
                             'VALUES(:company_id, :first_name, :last_name, :middle_name, :phone, :email, :avatar_url)'),
    }

    def __init__(self, engine) -> None:
        self.db = create_engine(engine)

    def execute_query(self, query, **params):
        try:
            with self.db.connect() as connection:
                result = connection.execute(query, **params)
                connection.commit()
                return result
        except Exception as _ex:
            print("[INFO] Error SQL", _ex)
            return None

    def create_company(self, company_name: str, description: str):
        return self.execute_query(self.query['create_company'], name=company_name, description=description)

    def delete_company(self, company_id: int):
        return self.execute_query(self.query['delete_company'], company_id=company_id)

    def last_company_id(self):
        result = self.execute_query(self.query['max_company_id'])
        return result.fetchone()[0] if result else None

    def create_employer(self, company_id: int, first_name: str, last_name: str, middle_name: str, phone: str, email: str = None, avatar_url: str = None):
        return self.execute_query(self.query['item_INSERT'], company_id=company_id, first_name=first_name, last_name=last_name, middle_name=middle_name, phone=phone, email=email, avatar_url=avatar_url)

    def get_list_employer(self, company_id: int):
        result = self.execute_query(self.query['list_SELECT'], id=company_id)
        return result.fetchall() if result else []

    def get_employer_id(self, company_id: int):
        result = self.execute_query(self.query['maxID_SELECT'], c_id=company_id)
        return result.fetchone()[0] if result else None

    def update_employer_info(self, new_name: str, employer_id: int):
        return self.execute_query(self.query['item_UPDATE'], new_name=new_name, employer_id=employer_id)

    def delete_employer(self, id: int):
        return self.execute_query(self.query['item_DELETE'], id_delete=id)