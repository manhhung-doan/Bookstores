from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='user',
            email='user@email.com',
            password='user123456'
        )

        self.assertEqual(user.username, 'user')
        self.assertEqual(user.email, 'user@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        super_user = User.objects.create_superuser(
            username='superuser',
            email='superuser@email.com',
            password='superuser123456'
        )

        self.assertEqual(super_user.username, 'superuser')
        self.assertEqual(super_user.email, 'superuser@email.com')
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)
