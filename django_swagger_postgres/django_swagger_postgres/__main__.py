import subprocess
import sys

def main():
    print("Запуск Django.")
    result = subprocess.run([sys.executable, '\DjangoSwaggerPG\django_swagger_postgres\manage.py', 'runserver'])


if __name__ == "__main__":
    main()