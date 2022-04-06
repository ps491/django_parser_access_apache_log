from django.test import Client, TestCase
from django.contrib.auth.models import User
from app_logs_apache.models import ApacheAccessLog


class Test(TestCase):

    def setUp(self):
        ApacheAccessLog.objects.create(
            ip="111.111.111", date="2022-05-04 10:00:00", data="some data")

    def test_all_labels(self):
        fields = {
            'ip': 100,
            'data': 100, }
        verbose_names = ('ip', 'data')
        for idx, el in enumerate(fields.items()):
            log = ApacheAccessLog.objects.get(id=1)
            field_label = log._meta.get_field(el[0]).verbose_name
            self.assertEquals(field_label, verbose_names[idx])
            max_length = log._meta.get_field(el[0]).max_length
            try:
                self.assertEquals(max_length, el[1])
            except AssertionError:
                raise ValueError(el[0])

    def test_object_name_is_ip_comma_date(self):
        log = ApacheAccessLog.objects.get(id=1)
        expected_object_name = '%s, %s' % (log.ip, log.date)
        self.assertEquals(expected_object_name, str(log))


class TestAdminPanel(TestCase):

    def create_user(self):
        self.username = "test_admin"
        self.password = User.objects.make_random_password()
        user, created = User.objects.get_or_create(username=self.username)
        user.set_password(self.password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        self.user = user

    def test_spider_admin(self):
        self.create_user()
        client = Client()
        client.login(username=self.username, password=self.password)
        admin_pages = [
            "/admin/",
            # put all the admin pages for your models in here.
            "/admin/auth/",
            "/admin/auth/group/",
            "/admin/auth/group/add/",
            "/admin/auth/user/",
            "/admin/auth/user/add/",
            "/admin/password_change/"
        ]
        for page in admin_pages:
            resp = client.get(page)
            assert resp.status_code == 200
           # assert "<!DOCTYPE html" in resp.content
