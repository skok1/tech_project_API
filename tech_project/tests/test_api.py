from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from task_app.models import Task, Category


class TaskAPITests(APITestCase):
    # we create a first Task object at database for test methods
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='sk0k1', password='userpassword1')
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(title='Test Category')
        self.task = Task.objects.create(title='Test Task', description='Test Description', user=self.user,
                                        category=self.category)

    def test_create_task(self):
        url = '/api/v1/task/'
        data = {
            'title': 'New Task',
            'description': 'New Description',
            'user': self.user.id,
            'category': self.category.pk
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)  # already had 1 object in setUp func

    def test_retrieve_task(self):
        url = '/api/v1/task/{}/'.format(self.task.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')  # check correct task is retrieved from setUp

    def test_update_task(self):
        url = '/api/v1/task/{}/'.format(self.task.id)
        data = {
            'title': 'Updated Task',
            'description': 'Updated Description'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()  # we need refresh base to see results
        self.assertEqual(self.task.title, 'Updated Task')  # checking equal 'title': 'Updated Task',

    def test_delete_task(self):
        url = '/api/v1/task/{}/delete/'.format(self.task.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(pk=self.task.id).exists())  # checking we had this object after delete
        # if we will get True - error else False - HTTP_204_NO_CONTENT

    def test_authentication(self):
        self.client.logout()  # firstly we must log out
        # at previous tests i did not log in operations because we have already
        url = '/api/v1/task/{}/'.format(self.task.id)
        data = {
            'title': 'New Task',
            'description': 'New Description',
            'user': self.user.id,
            'category': self.category.id
        }
        # WE NEED TO CHECK delete, create and update methods for unauthorized users
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)


class CategoryAPITests(APITestCase):
    # we create a first Category object at database for test methods
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='test', password='test')
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(title='Test Category')

    def test_create_category(self):
        url = '/api/v1/category/'
        data = {
            'title': 'New Category'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)  # already had 1 object in setUp func

    def test_retrieve_category(self):
        url = '/api/v1/category/{}/'.format(self.category.pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Category')  # check correct value is retrieved from setUp

    def test_update_category(self):
        url = '/api/v1/category/{}/'.format(self.category.pk)
        data = {
            'title': 'Updated category'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()  # we need refresh base to see results
        self.assertEqual(self.category.title, 'Updated category')  # checking equal 'title': 'Updated Task',

    def test_delete_category(self):
        url = '/api/v1/category/{}/delete/'.format(self.category.pk)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(pk=self.category.id).exists())  # checking we had this object after
        # delete
        # if we will get True - error else False - HTTP_204_NO_CONTENT

    def test_authentication_category(self):
        self.client.logout()  # firstly we must log out
        # at previous tests I did not log in operations because we have already
        url = '/api/v1/category/{}/'.format(self.category.id)
        data = {
            'title': 'New Task'
        }
        # WE NEED TO CHECK delete, create and update methods for unauthorized users
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)
