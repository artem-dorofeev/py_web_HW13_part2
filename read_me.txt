!!!мої нотатки. скопіювати та видалити !!!

оточення:
    poetry add django pymongo psycopg2 mongoengine

створюємо web проєкт:
    django-admin startproject hw10

створюємо quotes users:
    py .\manage.py startapp quotes
    py .\manage.py startapp users

запуск сервера:
    cd .\hw10\
    py .\manage.py runserver 
((hw10-local-py3.11) C:\Python\GIT\py_web_HW10\hw10>py .\manage.py runserver)

записываем цитаты в базу:
    py add_quotes_to_mongo.py

коннект до бд монго - створюємо utils.py в quotes


для міграції створюємо quotes\models.py
    py .\manage.py makemigrations
    применяем
    py .\manage.py migrate

hw10/db.sqlite3 - наша бд


створюємо utils\maigration.py

додати дані в вд:
    py -m utils.migration

запускаю постгрес, и в файле settings.py роблю зміни:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '567234',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

роблю миграцію:
    py .\manage.py migrate

створюю суперюзера:
    python manage.py createsuperuser
    artem   a.dorofeev@ukr.net  qawsedrftg


email:
    a.dorofeev_79@meta.ua
    1q2w#E$R%T

.env
SECRET_KEY=django-insecure-bf4fcujbr81all1x!ja0!24wz!p$h=lxq)o96$t!h%v)9(cdkj

DATABASE_NAME=hw10
DATABASE_USER=postgres
DATABASE_PASSWORD=567234
DATABASE_HOST=127.0.0.1
DATABASE_PORT=5432


EMAIL_HOST=smtp.meta.ua
EMAIL_PORT=465
EMAIL_HOST_USER=a.dorofeev_79@meta.ua
EMAIL_HOST_PASSWORD=1q2w#E$R%T


# DATABASE_ENGINE=django.db.backends.sqlite3
DATABASESQL_NAME= BASE_DIR / 'db.sqlite3'