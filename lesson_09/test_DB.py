from sqlalchemy import create_engine, inspect, text
# Импортируем необходимые функции из библиотеки SQLAlchemy:
# - create_engine: для подключения к базе данных
# - inspect: для получения информации о структуре базы
# - text: для написания SQL-запросов с параметрами

# Строка подключения к базе данных PostgreSQL:
# Формат: postgresql://<пользователь>:<пароль>@<хост>:<порт>/<имя_базы>
db_connection_string = "postgresql://postgres:123@localhost:5432/QA"

# Создаем объект подключения к базе данных
db = create_engine(db_connection_string)


# Проверка подключения и получения списка таблиц в базе
def test_db_connection():
    inspector = inspect(db)  # Создаем инспектор для получения метаданных о БД
    # Получаем список названий всех таблиц в базе
    names = inspector.get_table_names()
    # Проверяем, что вторая таблица называется 'subject'
    assert names[1] == 'subject'


# Выполнение запроса select * from student
def test_select():
    connection = db.connect()  # Устанавливаем соединение с базой данных
    result = connection.execute(text("SELECT * FROM student"))

    # Получаем все строки как список словарей (ключ — имя столбца)
    rows = result.mappings().all()
    row1 = rows[0]  # Получаем первую строку из результата

    # Проверка
    assert row1['user_id'] == 42568
    assert row1['level'] == "Pre-Intermediate"

    connection.close()  # Закрываем соединение с базой


# Функция для вставки новой строки в таблицу
def test_insert():
    connection = db.connect()  # Устанавливаем соединение с базой данных
    # Начинаем транзакцию (важно для операций изменения данных)
    transaction = connection.begin()

    sql = text("INSERT INTO subject(\"subject_title\") VALUES (:new_name)")

    # Выполняем запрос, передавая значение параметра :new_name
    connection.execute(sql, {"new_name": "Chemistry"})

    transaction.commit()

    connection.close()  # Закрываем соединение


def test_update():
    connection = db.connect()  # Устанавливаем соединение с базой данных
    transaction = connection.begin()  # Начинаем транзакцию

    sql = text("UPDATE subject SET"
               " subject_title = :sub WHERE subject_id = :id")
    connection.execute(sql, {"sub": "New sub", "id": 1})

    transaction.commit()  # Подтверждаем изменения
    connection.close()  # Закрываем соединение


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM subject WHERE (\"subject_title\") = (:new_name)")
    connection.execute(sql,  {"new_name": "Chemistry"})

    transaction.commit()
    connection.close()
