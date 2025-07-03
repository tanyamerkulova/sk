from ProjectsApi import ProjectsApi


api = ProjectsApi("https://ru.yougile.com/api-v2")


# получить список проектов
def test_get_project():
    body = api.get_project_list()
    assert len(body) > 0


# создать проект
def test_create_project():
    body = api.get_project_list()  # Получаем и сохраняем список
    len_before = len(body)  # Находим длину переменной
    # Создать новый проект
    title = "Autotest"
    users = "admin"
    api.create_project(title, users)

    # Получить количество проектов после
    body = api.get_project_list()
    len_after = len(body)  # Находим длину переменной
    assert len_after - len_before == 1


def test_create_project_negative():
    users = "admin"
    title = ""
    response = api.create_project(title, users)

    # Проверяем, что API вернул ошибку с кодом 400
    assert response["statusCode"] == 400
    # Проверяем, что title не может быть пустым
    assert "title should not be empty" in response["message"][0]


# изменение проекта
def test_edit():
    # Создать новый проект
    title = "Autotest Edit"
    users = "admin"
    result = api.create_project(title, users)
    new_id = result["id"]

    new_title = "Updated Edit"
    id_edit = api.edit_project(new_id, new_title)['id']
    # Обращаемся к проекту
    new_company = api.get_project_by_id(id_edit)
    # Проверяем, что название проекта поменялось
    assert new_company["title"] == new_title


def test_edit_negative():
    project_id = 99999  # Не существующий ID
    new_title = "No Project"

    # Попытка обновить проект с несуществующим ID
    # Проверяем, что API возвращает ошибку с кодом 404 (Not Found)
    assert api.edit_project(project_id, new_title)["statusCode"] == 404
    # Проверяем, что тип ошибки указан как "Not Found"
    assert api.edit_project(project_id, new_title)["error"] == "Not Found"


# получить компанию по ID
def test_get_one_project():
    # Создать новый проект
    title = "Autotest ID"
    users = "admin"
    result = api.create_project(title, users)
    new_id = result["id"]

    # Обращаемся к проекту
    new_company = api.get_project_by_id(new_id)
    id_emp = f"{api.get_id_employee()}"
    # Проверим название, описание
    assert new_company["title"] == title
    assert new_company["users"][id_emp] == users


def test_get_one_project_negative():
    project_id = 99999  # Не существующий ID
    # Попытка получить проект с несуществующим ID
    # Проверяем, что статус код 404 (Not Found)
    assert api.get_project_by_id(project_id)["statusCode"] == 404
    assert api.get_project_by_id(project_id)["error"] == "Not Found"
