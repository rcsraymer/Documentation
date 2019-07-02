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
(Dev-JlwXeuLe) C:\Dev>django-admin startproject project_name
(Dev-JlwXeuLe) C:\Dev>cd project_name
```
If using VS Code, select the correct environment for the Python interpreter.  CTRL-Shift-P. Type Python. Select Interpreter, and choose the one that has your folder name and pipenv.  
  
Generate app:
```console
(Dev-JlwXeuLe) C:\Dev\project_name>python manage.py startapp app_name
```

Go into _project_name/settings.py_.  
Add _app_name_ and _rest_framework_ to **_INSTALLED_APPS_**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_name',
    'rest_framework',
]
```

Go to app_name and create models.  
_example:_
```python
from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Quizzes"
```
