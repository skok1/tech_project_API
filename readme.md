<center> DOCUMENTATION  </center>
-



>This application was built using PostgreSQL and the Django REST Framework. The application supports four types of requests: PUT, CREATE, GET, and DELETE, which symbolize CRUD operations.

### First steps:

1.Clone the repository to your local machine.

2.Navigate to the project directory.

3.Open a terminal or command prompt.

4.Run the following command to start the application:

The file for the text database is left in the description. To connect the file, you need to use the command: 

```
docker-compose up --build
```

After that, you need to enter the Django container in another console and perform migration for this container:

```
docker ps    # use cintainer id from this result

docker exec -it <container id> bash 

python manage.py migrate   
```

At the file task_app/urls.py we have 9 type of links:
```
urlpatterns = [
    path('api/v1/task/', TaskCreateAPI.as_view()),
    path('api/v1/task/<int:pk>/', TaskUpdateAPI.as_view()),
    path('api/v1/task/<int:pk>/delete/', TaskDeleteAPI.as_view()),
    path('api/v1/category/', CategoryCreateAPI.as_view()),
    path('api/v1/category/<int:pk>/', CategoryUpdateAPI.as_view()),
    path('api/v1/category/<int:pk>/delete/', CategoryDeleteAPI.as_view()),
    path('api/v1/session_auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
```
We can authorize use 'session-based authentication' or 'djoser packet'. If you want use a djoser you can check commands at the documentation. This packet include a lot of useful commands like create, delete, authorize user and else.

## Accessing API Endpoints

### Endpoints:

- You must use 'task' or 'category' instead of 'my_object' 

> PUT .../api/v1/my_object/1/: Update a specific resource
> 
> POST .../api/my_object/: Create a new resource
>
> GET .../api/v1/my_object/: Get all information in JSON format
> 
> GET .../api/v1/my_object/1/: Get information about specific resource
> 
> DELETE .../api/v1/my_object/1/delete/: Delete a specific resource


### Example Usage

Update: (send PUT request)

> http://localhost:8000/api/v1/my_object/1/
> 
Delete: (send DELETE request)
>
> http://localhost:8000/api/v1/my_object/1/delete/
> 
Create: (send POST request)
> 
> http://localhost:8000/api/v1/my_object/
> 
Read all: (send GET request)
> http://localhost:8000/api/v1/my_object/
> 
Read ONE object(task or category): (send GET request)
> http://localhost:8000/api/v1/my_object/1/

Additionally, I have covered with tests the execution of requests for both authorized and unauthorized users. Test file location: 'tech_project/test_api.py'. I have a 2 classes for categories and tasks


