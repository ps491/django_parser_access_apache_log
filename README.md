Запуск в Windows:

1. Установить WSL запустить и настроить пользователя  (Ubuntu 20.04LTS)

2. Настройка WSL 
    1) wsl -l -v
    2) wsl --set-default-version 2

3. Настройка VS CODE (CTRL+SHIFT+P) 
Установить расширения:
    1) Django
    2) GitHub Pull Requests and Issues
    3) gitignore
    4) Pylance
    5) Python
    6) Python Preview
    7) Remote - WSL
    8)Подключиться к WSL (VS CODE)

5. В терминале:
    1) sudo apt install -y python3-venv
    2) mkdir myapp && cd myapp
    3) python3 -m venv .venv
    5) выбрать интерпретатор python
    6) source .venv/bin/activate
    4) cd myapp 
    5) git clone https://github.com/POMXARK/django_parser_access_apache_log.git
    6) pip install -r requirements.txt
 
 5. Настройка Ubuntu:
    1) nano visudo
    2) добавить в конец %sudo ALL=NOPASSWD: /usr/sbin/service cron start
    3) usermod -a -G crontab имя_пользователя_ubuntu_с_root_правами
    1) sudo service cron start
    2) sudo service apache2 start
    3) hostname -I

 6. Запуск проекта
    1) cd project
    2) python manage.pu migrate
    3) python manage.py createsuperuser
    4) python manage.py runserver
    5) python manage.py cron add

 7. Тестирование apache2 access.log:
    1) hostname/несуществующая_страница

 8. Тестрование Api:
    1) /api/apache_logs/
    2) /api/apache_logs/?ip=172.23.32
    3) /api/apache_logs/?date_after=2022-04-04&date_before=2022-04-04

 9. Ссылки на доп материалы:
    1) https://docs.microsoft.com/ru-ru/windows/wsl/install-manual
    2) https://docs.microsoft.com/en-us/windows/wsl/basic-commands
    3) https://netpoint-dc.com/blog/python-venv-ubuntu-1804/
    4) https://alimuradov.ru/ispolzovanie-cron-v-podsisteme-linux-wsl-v-windows-10/
    5) https://realpython.com/python-assert-statement/
    6) https://www.vinta.com.br/blog/2017/how-i-test-my-drf-serializers/

10. Unit-тестрирование
   1) python manage.py test
   2) coverage run --source='.' manage.py test .
   3) coverage report
   4) coverage html

11. Установка с Docker
   1) docker build .

   Пароль и логин от тестовой базы admin/admin
