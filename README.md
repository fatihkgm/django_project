# django_project

Terminal 
pip install django

version of django 
python -m django --version

create an folder //cd folder
django-admin

django-admin startproject nameproject

cd to folder

folder name here
tree


to open the project 
python manage.py runserver   // we can see http localhost

//you can use local use localhost8000

//localhost8000/admin

url.py 
//you will path admin/admin.site.urls allows us to access

stop runnuning control c

a

python manage.py startapp blog





after we created template and blog in one folder html
folder > app.py copy logConfig

then go > project > setting >install_app copy past 'blog.apps.blogConfig',




Admin
localhost://8000/admin
//python manage.ph createsuperuser   //no such table accour

we should run migration for database

python manage.py makemigrations
//no changes detected

In order to apply to migration 
python manage.py migrate

python manage.py createsuperuser 

name email password 1234

Anither User
TestUser
mnbvcxz1234


//DATABASE


