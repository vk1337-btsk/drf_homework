<h3 align="center">Сервис email рассылки сообщений на Django</h3>

<details>
  <summary>Оглавление</summary>
  <ol>
    <li>О проекте</li>
    <li>Технологии</li>
    <li>Настройка проекта</li>
    <li>Использование</li>
    <li>Контакты</li>
  </ol>
</details>



## О проекте

Сервис email рассылок. После регистрации вы сможете добавить клиентов, сообщение и создать рассылку,
выбрав дату начала и окончания рассылки и с какой периодичностью производить рассылку.
При наступлении даты отправки происходит автоматическая отправка сообщения вашим клиентам.

## Технологии
- Django
- PostgreSQL
- DRF


## Настройка проекта

Для работы с проектом произведите базовые настройки.

### 1. Клонирование проекта

Клонируйте репозиторий используя следующую команду.
  ```sh
  git clone https://github.com/vk1337-btsk/drf_homework.git
  ```


### 2. Настройка виртуального окружения и установка зависимостей

- Инструкция для работы через виртуальное окружение - poetry: 
```text
poetry init - Создает виртуальное окружение
poetry shell - Активирует виртуальное окружение
poetry install - Устанавливает зависимости
```

- Инструкция для работы через виртуальное окружение - pip:

Создает виртуальное окружение:
```text
python3 -m venv venv
```

Активирует виртуальное окружение:
```text
source venv/bin/activate          # для Linux и Mac
venv\Scripts\activate.bat         # для Windows
```

Устанавливает зависимости:
```text
pip install -r requirements.txt
```

### 3. Редактирование config.ini.sample:

- В корне проекта переименуйте файл config.ini.sample в config.ini и отредактируйте параметры:
    ```text
    [django_settings]
    DEBUG = True_or_False
    SECRET_KEY = your_secret_key
    
    
    [database]
    DB_ENGINE = postgresql_psycopg2
    DB_NAME = your_name_db
    DB_USER = your_user_db
    DB_PASSWORD = your_password_db
    DB_HOST = localhost
    DB_PORT = 5432
    ```

### 4. Настройка БД:

- Создать миграции:
  ```text
  python manage.py makemigrations
  ```

- Примените миграции:
  ```text
  python manage.py migrate
  ```