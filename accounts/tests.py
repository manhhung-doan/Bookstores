from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignupCreateView

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

class HomepageTests(TestCase):

    '''
    La fonction "setUp" a été pré-construit. Elle va rechercher le nom d'url qui est coresspondant\
    avec demande (ne peut pas changer de nom)
    '''
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    '''
    L1: Le test existe: pour vérifier si le code de HTTP status d'url dans la fonction "setUp" \
        est égal 200, ce qui signifie qu'il existe.\
    L2: Le test template: on peut comfimer que l'url utilise le template correct \
    L3 + L4: Le test HTML: on peut vérifier que le "homepage" a le bon HTML + texte ou pas
    '''
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, "S'inscrire")
        self.assertNotContains(self.response, "Un element au hasard")

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    '''
    Le test "resolve": vérifier la fonction "SignupCreateView" (dans accounts/views.py) a vraiment résolus un path d'URL donné \
    et le test ici va checker si le nom de "view" est correspondant avec "SignupCreateView" 
    '''
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupCreateView.as_view().__name__)