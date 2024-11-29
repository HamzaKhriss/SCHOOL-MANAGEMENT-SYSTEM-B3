import unittest
import os
import django
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'school_management.school_management.settings'
django.setup()

class TestSettings(unittest.TestCase):

    def test_debug(self):
        self.assertEqual(settings.DEBUG, True)

    def test_allowed_hosts(self):
        self.assertEqual(settings.ALLOWED_HOSTS, [])

    def test_installed_apps(self):
        self.assertIn('django.contrib.admin', settings.INSTALLED_APPS)
        self.assertIn('core', settings.INSTALLED_APPS)

    def test_middleware(self):
        self.assertIn('django.middleware.security.SecurityMiddleware', settings.MIDDLEWARE)
        self.assertIn('django.middleware.common.CommonMiddleware', settings.MIDDLEWARE)

    def test_database_settings(self):
        self.assertEqual(settings.DATABASES['default']['ENGINE'], 'django.db.backends.mysql')
        self.assertEqual(settings.DATABASES['default']['NAME'], 'school_management_db')
        self.assertEqual(settings.DATABASES['default']['USER'], 'root')
        self.assertEqual(settings.DATABASES['default']['PASSWORD'], 'root')
        self.assertEqual(settings.DATABASES['default']['HOST'], 'localhost')
        self.assertEqual(settings.DATABASES['default']['PORT'], '3306')

    def test_templates(self):
        self.assertTrue(settings.TEMPLATES[0]['APP_DIRS'])
        self.assertIn('django.template.context_processors.debug', settings.TEMPLATES[0]['OPTIONS']['context_processors'])

if __name__ == '__main__':
    unittest.main()    