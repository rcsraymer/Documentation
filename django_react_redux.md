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
# 2 - Implementing React
```console
(Dev-JlwXeuLe) C:\Dev\django-react\lead_manager>py manage.py startapp frontend
```
Get a new frontend folder from doing this. Now, we need to create a few new folders for React to live in.
```console
(Dev-JlwXeuLe) C:\Dev\django-react\lead_manager>mkdir -p ./frontend/src/components
(Dev-JlwXeuLe) C:\Dev\django-react\lead_manager>mkdir -p ./frontend/{static,templates}/frontend
```
Components - Holds the React app.
  
Static - Hosts compiled javascript.
  
Templates - Handles index.html that gets loaded.

```console
(Dev-JlwXeuLe) C:\Dev\django-react> npm init -y
(Dev-JlwXeuLe) C:\Dev\django-react> npm i -D webpack webpack-cli
(Dev-JlwXeuLe) C:\Dev\django-react> npm i -D @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties
(Dev-JlwXeuLe) C:\Dev\django-react> npm i react react-dom prop-types
```
Check package.json to ensure apps are installed.  
In root, create _.babelrc_ file:
```json
{
    "presets": ["@babel/preset-env", "@babel/preset-react"],
    "plugins": ["transform-class-properties"]
}
```
Create webpack config file in root: webpack.config.js
```javascript
module.exports = {
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            }
        ]
    }
}
```
in package.json, replace test with dev in scripts:
```json
"scripts": {
    "dev": "webpack --mode development --watch ./leadmanager/frontend/src/index.js --output ./leadmanager/frontend/static/frontend/main.js",    
    "build": "webpack --mode production ./leadmanager/frontend/src/index.js --output ./leadmanager/frontend/static/frontend/main.js"
},
```
Create index.js in frontend/src
```javascript
import App from './components/App';
```
Create App.js in components:
```javascript
import React, { Component } from 'react';
import ReactDOM from 'react-dom';

class App extends Component {
    render() {
        return <h1>React App</h1>
    }
}

ReactDOM.render(<App />, document.getElementById('app'));
```
Create templates/frontend/index.html:
```html
<body>
    <div id="app"></div>
    {% load static %}
    <script src="{% static "frontend/main.js" %}"></script>
    <-- Add bootstrap -->
</body>
```
In leadmanager app folder, goto settings.py. Add frontend to INSTALLED_APPS
```python
INSTALLED_APPS = [
    ...
    'frontend'
] 
```
in frontend folder, goto _views.py_:
```python
def index(request):
    return render(request, 'frontend/index.html')
```
In frontend, create _urls.py_
```python
from django.urls import path
from . import views

urlpatterns =[
    path('', views.index)
]
```
in _leadmanager/urls.py_:
```python
urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('leads.urls'))
]
```
```console
(Dev-JlwXeuLe) C:\Dev\django-react> npm run dev
```
Check static/frontend : ensure there is main.js which is the compiled javascript which then gets loaded into the template. Restart server and check the site in the browser to ensure the ReactApp is running.  
  
Install vs code extension: ES7/React/Redux/GraphQL/React-Native snippets  
 
In src/components create layout folder. Then header.js:
```javascript
import React, { Component } from 'react'

export class Header extends Component {
    render() {
        return (
            <-- insert navbar from bootstrap code here. change all reference to 'class' to 'className'. Remove form. Change Hidden Brand to Lead Manager. Remove li objects-->
        )
    }
}
```

Go to components _app.js_ and import Header

```javascript
...
import Header from './layout/Header';

class App extends Component {
    render() {
        return (
            <Header />
        )
    }
```
```console
(Dev-JlwXeuLe) C:\Dev\django-react> npm run dev
```
in components, create folder leads  
  
Create Dashboard.js and Form.js and Leads.js. Repeat process of creating class based components as described above for Form.js and Leads.js. For Dashboard.js, create a function based component:
  
```javascript
import React, { Fragment } from 'react';
import Form from './Form';
import Leads from './Leads';

export default function Dashboard() {
    return (
        <Fragment>
            <Form />
            <Leads />
        </Fragment>
    )
}
```
In App.js, import Dashboard:
```javascript
import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';

import Header from './layout/Header';
import Dashboard from './leads/Dashboard';

class App extends Component {
    render() {
        return (
            <Fragment>
                <Header />
                <div className="container">
                    <Dashboard />
                </div>
            </Fragment>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));
```
