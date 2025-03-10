Для запуска проекта необходимо внести изменения в файл settings.py. 
В настройках подключения (DATABASES =) указать свои параметры.
Выполнить миграцию с помощью следующих команд:
    python manage.py makemigrations
    python manage.py migrate
Запустить сервер:
    python manage.py runserver
После успешного запуска, документация SWAGGER будет доступна по адресу:
http://127.0.0.1:8000/swagger/