from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import *

# Create your tests here.

'''
Ici, on utilise "SimpleTestCase" parce q'il est un sous-ensemble spécial de "TestCase" \
et il est conçu pour page web qui n'a pas un modèle inclus. 
'''

class HomepageTests(SimpleTestCase):

    '''
    La fonction "setUp" a été pré-construit (ne peut pas changer de nom)
    '''
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    '''
    Des tests existent: pour vérifier si le code de HTTP status de "homepage" \
    est égal 200, ce qui signifie qu'il existe.
    '''
    def test_homepage_status_code(self):
        # response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)

    # def test_homepage_url_name(self):
        # response = self.client.get(reverse('home'))
        # self.assertEqual(self.response.status_code, 200)

    '''
    Des tests templates: en utilisant method "assertTemplateUsed", on peut comfimer que le "homepage" \
    utilise le template correct
    '''
    def test_homepage_template(self):
        # response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'home.html')

    '''
    Des tests HTML: en utilisant method "assertContains" ou "assertNotContains", on peut vérifier que le "homepage" \
    a le bon HTML + texte ou pas
    '''
    def test_homepage_contains_correct_html(self):
        # response = self.client.get('/')
        self.assertContains(self.response, 'Homepage')

    def test_homepage_template(self):
        # response = self.client.get('/')
        self.assertNotContains(self.response, 'Salut, je ne devrais pas être là!')

    '''
    Des tests "resolve": vérifier la fonction "HomePageView" (dans views.py) a vraiment résolus un path d'URL donné \
    et le test ici va checker si le nom de "view" est correspondant avec "HomePageView" 
    '''
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

