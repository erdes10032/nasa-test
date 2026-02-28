# NASA Slider Test Project

Тестовый проект на Django 5.2 с использованием:

- Bootstrap 5
- Slick Slider
- django-filer
- django-admin-sortable2
- MySQL

## Установка

Python 3.12+

Клонировать реопозиторий:
```bash
git clone https://github.com/erdes10032/nasa-test.git
cd nasa-test
```

Создать виртуальное окружение:
```bash
python -m venv venv
venv\Scripts\activate
```

Установить зависимости:

```bash
pip install -r req.pip
```

## Настройка

Заполнить .env файл своими данными

## Миграции
```bash
python manage.py migrate
```

Создать суперпользователя:

```bash
python manage.py createsuperuser
```

## Запуск

```bash
python manage.py runserver
```

Главная страница
http://localhost:8000/

Админ-панель:
http://localhost:8000/admin

Чтобы на странице появились фото, необходимо их добавить через админ-панель

Слайды добавляются через django-filer.
Поддерживается drag & drop сортировка.
