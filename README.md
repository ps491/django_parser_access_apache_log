Launch on Windows:

1. Install WSL run and configure user (Ubuntu 20.04LTS)

2. WSL setup
    1) wsl -l -v
    2) wsl --set-default-version 2

3. Customize VS CODE (CTRL+SHIFT+P)
Install extensions:
    1) Django
    2) GitHub Pull Requests and Issues
    3) gitignore
    4) Pylance
    5) Python
    6) Python Preview
    7) Remote - WSL
    8) Connect to WSL (VS CODE)

5. In the terminal:
    1) sudo apt install -y python3-venv
    2) mkdir myapp && cd myapp
    3) python3 -m venv .venv
    5) select python interpreter
    6) source .venv/bin/activate
    4) cd myapp
    5) git clone https://github.com/POMXARK/django_parser_access_apache_log.git
    6) pip install -r requirements.txt
 
 5. Ubuntu setup:
    1) nano visudo
    2) add to the end %sudo ALL=NOPASSWD: /usr/sbin/service cron start
    3) usermod -a -G crontab ubuntu_root_username
    1) sudo service cron start
    2) sudo service apache2 start
    3) hostname -I

 6. Project launch
    1) cd project
    2) python manage.pu migrate
    3) python manage.py createsuperuser
    4) python manage.py runserver
    5) python manage.py cron add

 7. Testing apache2 access.log:
    1) hostname/non-existent_page

 8. API testing:
    1) /api/apache_logs/
    2) /api/apache_logs/?ip=172.23.32
    3) /api/apache_logs/?date_after=2022-04-04&date_before=2022-04-04

 9. Links to additional materials:
    1) https://docs.microsoft.com/ru-ru/windows/wsl/install-manual
    2) https://docs.microsoft.com/en-us/windows/wsl/basic-commands
    3) https://netpoint-dc.com/blog/python-venv-ubuntu-1804/
    4) https://alimuradov.ru/ispolzovanie-cron-v-podsisteme-linux-wsl-v-windows-10/
    5) https://realpython.com/python-assert-statement/
    6) https://www.vinta.com.br/blog/2017/how-i-test-my-drf-serializers/

10. Unit testing
   1) python manage.py test
   2) coverage run --source='.' manage.py test .
   3) coverage report
   4) coverage html

11. Installation with Docker
   1) docker build .

   Password and login from the test database admin/admin