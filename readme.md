Для запуска проекта необходимо в файле settings.py внести изменения. 
В настройках подключения указать имя сервера пользователя и пароль
CREATE ROLE "user" WITH LOGIN NOINHERIT CREATEDB PASSWORD 'user';

CREATE DATABASE djangodb WITH OWNER = "user" ENCODING = 'UTF8';

После успешного запуска, документация SWAGGER будет доступна по адресу:
http://127.0.0.1:8000/swagger/