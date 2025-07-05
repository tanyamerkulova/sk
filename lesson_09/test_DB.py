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
    names = inspector.get_table_names()  # Получаем список названий всех таблиц в базе
    assert names[1] == 'subject'  # Проверяем, что вторая таблица называется 'subject'

# Выполнение запроса select * from student
def test_select():
    connection = db.connect()  # Устанавливаем соединение с базой данных
    result = connection.execute(text("SELECT * FROM student"))  # Выполняем SQL-запрос

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
    transaction = connection.begin()  # Начинаем транзакцию (важно для операций изменения данных)

    sql = text("INSERT INTO subject(\"subject_title\") VALUES (:new_name)")
    
    # Выполняем запрос, передавая значение параметра :new_name
    connection.execute(sql, {"new_name": "Chemistry"})

    transaction.commit()  # Подтверждаем транзакцию, чтобы изменения сохранились в базе

    result = connection.execute(text("SELECT * FROM subject WHERE subject_title = :new_name"),
                                {"new_name": "Chemistry"}).mappings().first()
    
    assert result is not None
    assert result["subject_title"] == "Chemistry"

    connection.close()  # Закрываем соединение


def test_update():
    connection = db.connect()  # Устанавливаем соединение с базой данных
    transaction = connection.begin()  # Начинаем транзакцию

    sql = text("UPDATE subject SET subject_title = :sub WHERE subject_id = :id")
    connection.execute(sql, {"sub": "New sub", "id": 1})

    transaction.commit()  # Подтверждаем изменения
    
    result = connection.execute(text("SELECT subject_title FROM subject WHERE subject_id = :id"),
                                {"id": 1}).mappings().first()
    assert result is not None
    assert result["subject_title"] == "New sub"
    
    connection.close()  # Закрываем соединение


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM subject WHERE (\"subject_title\") = (:new_name)")
    connection.execute(sql,  {"new_name": "Chemistry"})

    transaction.commit()

    result = connection.execute(text("SELECT * FROM subject WHERE subject_title = :new_name"),
                                {"new_name": "Chemistry"}).mappings().first()
    
    assert result is None  # Запись должна отсутствовать
    connection.close()

