import requests


class ProjectsApi:
    # Инициализация
    def __init__(self, url) -> None:
        self.url = url

    # Получить id
    def get_id(self, user="", password=""):
        creds = {
            "login": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/companies', json=creds)
        return resp.json()["content"][0]["id"]

    # Получить ключ API
    def get_key(self,  user="", password=""):
        companyId = self.get_id()
        creds = {
            "login": user,
            "password": password,
            "companyId": f"{companyId}"
        }
        print(creds)
        resp = requests.post(self.url + '/auth/keys', json=creds)
        return resp.json()["key"]

    # headers
    def my_headers(self):
        token = self.get_key()
        # создание
        my_headers = {}
        my_headers["Authorization"] = f"Bearer {token}"
        return my_headers

    # Получить список проектов
    def get_project_list(self):
        resp = requests.get(self.url + '/projects',
                            headers=self.my_headers())
        return resp.json()['content']

    # Получить id сотрудника
    def get_id_employee(self):
        resp = requests.get(self.url + '/users',
                            headers=self.my_headers())
        return resp.json()["content"][0]["id"]

    # Создать проект
    def create_project(self, title="", users=""):
        id = self.get_id_employee()
        company = {
                "title": title,  # "СкайПро"
                "users": {
                    f"{id}": users  # "admin"
                }
        }
        print(company)
        resp = requests.post(self.url + '/projects',
                             json=company, headers=self.my_headers())
        return resp.json()

    def get_id_project(self):
        resp = requests.get(self.url + '/projects',
                            headers=self.my_headers())
        return resp.json()['content'][0]

    # Изменить проект
    def edit_project(self, new_id, new_name):
        # Формируем URL
        url_with_id = f"{self.url}/projects/{new_id}"

        # Вызываем словарь
        company = {
            "title": new_name,  # Новое название проекта
        }

        # Метод отправляет запрос по URL, передает заголовки и тело
        resp = requests.put(url_with_id, json=company,
                            headers=self.my_headers())

        return resp.json()

    # Получить по id
    def get_project_by_id(self, pr_id):
        resp = requests.get(f"{self.url}/projects/{pr_id}",
                            headers=self.my_headers())
        return resp.json()
