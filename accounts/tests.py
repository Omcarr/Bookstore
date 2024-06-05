from django.test import TestCase

# Create your tests here.
#always write unit tests for specific functions
#integrations tests for features which are bigger, multiscreen or more vulnerable to failure
#a good djnago app has many unit tests and few integrations tests
from django.contrib.auth import get_user_model
from django.test import TestCase
class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
        username="omcarr", email="omkar.yadav1809@gmail.com", password="testpass123"
        )
        self.assertEqual(user.username, "omcarr")
        self.assertEqual(user.email, "omkar.yadav1809@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
        username="superadmin", email="superadmin@email.com", password="testpass123"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)