# Full Stack React & Django
Refer to the [YouTube Series]("https://www.youtube.com/watch?v=Uyei2iDA4Hs") of the same name.    

For further documentation, refer to [https://www.django-rest-framework.org/]("https://www.django-rest-framework.org/")  
## 1 - Basic REST API  
Need to install pipenv. This is a packaging tool for Python that consolidates and simplifies the dev process to a single command line tool. 

```console
C:\Dev>pip3 install pipenv
```
Using pip3 instead of pip installs something globally. Once we have pipenv we can create a virtual environment and then install anything in that virtual environment.
```console
C:\Dev>pipenv shell
```
This creates the virtual environment for the project. It then creates the pip file in your working directory.
```console
(Dev-JlwXeuLe) C:\Dev>code .
```
This opens VS Code in your directory.
```console
(Dev-JlwXeuLe) C:\Dev>pipenv install django djangorestframework djang-rest-knox
```
These are added to the packages in the pipfile. A lockfile is also created with all the dependencies and versions.  
  
Create the project:
```console
(Dev-JlwXeuLe) C:\Dev\django-react>django-admin startproject lead_manager
(Dev-JlwXeuLe) C:\Dev\django-react>cd lead_manager
```
If using VS Code, select the correct environment for the Python interpreter.  CTRL-Shift-P. Type Python. Select Interpreter, and choose the one that has your folder name and pipenv.  
  
Generate app:
```console
(Dev-JlwXeuLe) C:\Dev\django-react\lead_manager>python manage.py startapp leads
```

Go into lead_manager folder and open _settings.py_.  
  
Add _leads_ and _rest_framework_ to **_INSTALLED_APPS_**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'leads',
    'rest_framework',
]
```

Go to leads app and create models.
```python
from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True) # blank=True allows message to be optional
    created_at = models.DatTimeField(auto_now_add=True)
```

Create and run migrations:
```console
(Dev-JlwXeuLe) C:\Dev\django-react\lead_manager>python manage.py makemigration leads
(Dev-JlwXeuLe) C:\Dev\django-react\lead_manager>python manage.py migrate
```
We now need to create a serializer to take our model (our queryset of leads) and turn it into JSON.
1. Go to _leads_ app folder
2. Create a file called _serializers.py_
```python
from rest_framework import serializers
from leads.models import Lead

# Lead Serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
```
We need to now create our api.
1. Create a file called _api.py_
```python
from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
```
Now we need to create our URLs.  
  
If we look in lead_manager, there is a root _urls.py_ file. By default, there is an admin url pattern. For the purpose of this tutorial, that will not be used.  
  
Change file to look like this:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns =[
    path('', include('leads.urls')),
]
```
We now need a urls file in _leads_

1. Go to _leads_ app folder
2. Create a file called _urls.py_
```python
from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads') # endpoint is api/leads, pass in viewset

urlpatterns = router.urls
```
This API should provide basic CRUD functionality to our application.  
  
Can test this by running the django server and interacting with the API via Postman.

```console
(Dev-JlwXeuLe) C:\Dev\django-react\lead_manager>python manage.py runserver
```
