import allure
from API import ApiEmployee
from API import Company
from data_base import DbEmployee

db = DbEmployee(
    "postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0"
    )

company = Company("https://x-clients-be.onrender.com")

param_id = "?company=" + str(company.get_id_company())

company_id = company.get_id_company()

api = ApiEmployee("https://x-clients-be.onrender.com")

body = {
    "id": 1010108711,
    "firstName": "string",
    "lastName": "string",
    "middleName": "string",
    "companyId": company_id,
    "email": "string@bl.yu",
    "url": "string",
    "phone": "string",
    "birthdate": "2023-08-14T11:02:45.622Z",
    "isActive": "true"
}


@allure.title("Получение списка сотрудников.")
@allure.description("Проверка получения списка сотрудников.")
@allure.feature("GET")
@allure.severity("Major")
def test_get_list_employee2():
    with allure.step("Получение списка сотрудников через API"):
        api_result = api.get_list_employee2(param_id)
        api_result = api_result.json()
    with allure.step("Получение списка сотрудников через DB"):
        db_result = db.get_list_employee(company_id)
    with allure.step("Сравнение списков"):
        assert len(api_result) == len(db_result)


@allure.title("Добавление нового сотрудника через API .")
@allure.description("Проверка добавления нового сотрудника.")
@allure.feature("POST")
@allure.severity("Critical")
def test_add_employee2():
    with allure.step("Получить сотрудников через БД"):
        db_result = db.get_list_employee(company_id)
    with allure.step("Создание сотрудника через API"):
        api.add_new_employee2(body)
        api_response = api.get_list_employee2(param_id)
        api_response = api_response.json()
    with allure.step("Проверка что список увичился на 1"):
        assert len(api_response)-len(db_result) == 1


@allure.title("Получение данных сотрудника по ID.")
@allure.description("Тест на получение данных сотрудника по ID.")
@allure.feature("GET")
@allure.severity("Major")
def test_get_new_employee2():
    with allure.step("Получение ID сотрудника через API"):
        resp = api.get_list_employee2(param_id)
        api_new_employee = resp.json()[-1]['id']
    with allure.step("Получение ID сотрудника через БД"):
        db_new_employee = db.get_id_new_employee()
    with allure.step("Сравнение ID"):
        assert api_new_employee == db_new_employee


@allure.title("Добавление нового сотрудника.")
@allure.description("Проверка добавления нового сотрудника.")
@allure.feature("POST")
@allure.severity("Blocker")
def test_create_employee():
    with allure.step("Создание сотрудника через БД"):
        db.add_new_employee("Юрий", "Горбатенко", "891294443688", True,
                            company_id)
        data_employee = api.get_new_employee2(db.get_id_new_employee())
        data_employee = data_employee.json()
    with allure.step("Проверка данных сотрудника"):
        assert data_employee["firstName"] == "Юрий"
        assert data_employee["lastName"] == "Горбатенко"
        assert data_employee["phone"] == "891294443688"
        assert data_employee["isActive"] == True
        assert data_employee["companyId"] == company_id
    id = db.get_id_new_employee()
    db.delete(id)


@allure.title("Изменение данных о новом сотруднике.")
@allure.description("Изменение данных о новом сотруднике.")
@allure.feature("PATCH")
@allure.severity("Blocker")
def test_edit_employee():
    with allure.step("Содание сотрудника"):
        db.add_new_employee("Юрий", "Горбатенко", "891294443688", True,
                            company_id)
        id = db.get_id_new_employee()
    with allure.step("Изменение данных сотрудника"):
        db.edit_employee("Иван", "Петров", "0987654321", True, company_id, id)
    data_employee = api.get_new_employee2(id)
    data_employee = data_employee.json()
    with allure.step("Проверка измененных данных сотрудника"):
        assert data_employee["firstName"] == "Иван"
        assert data_employee["lastName"] == "Петров"
        assert data_employee["phone"] == "0987654321"
        assert data_employee["isActive"] == True
        assert data_employee["companyId"] == company_id
    id = db.get_id_new_employee()
    db.delete(id)
