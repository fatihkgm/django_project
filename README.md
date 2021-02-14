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
in orde to update databse
(base) test@iMac django_project % python manage.py makemigrations  
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post

python manage.py sqlmigrate blog 0001

//to run and change affect 
python manage.py migrate

(with migration make change force )

python manage.py shell

user = User.objects.filter(username='CoreyMS').first()


In [13]: user                                                                   
Out[13]: <User: fatih>

In [14]: user.id                                                                
Out[14]: 1

In [15]: user.pk                                                                
Out[15]: 1

In [16]: user = User.objects.get(id=1)                                          

In [17]: user                                                                   
Out[17]: <User: fatih>

In [18]:  


In [22]: post_1 = Post(tittle='Blog 1',content='First Post Content' , author=user)                 

In [23]: Post.objects.all()                                                                        
Out[23]: <QuerySet []>

In [24]:  In [23]: Post.objects.all()                                                                        
Out[23]: <QuerySet []>

In [24]: post_1.save()                                                                             

In [25]: Post.objects.all()                                                                        
Out[25]: <QuerySet [<Post: Post object (1)>]>


zsh: suspended  python manage.py shell
(base) test@iMac django_project % python manage.py shell
Python 3.7.7 (default, May  6 2020, 04:59:01) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.16.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from blog.models import Post                                                               

In [2]: from django.contrib.auth.models import User                                                

In [3]:  
Post.objects.all()                                                                         
Out[3]: <QuerySet [<Post: Post object (1)>]>


Post.objects.all()                                                                         
Out[3]: <QuerySet [<Post: Post object (1)>]>

In [4]: User.objects.filter(username='fatih').first()                                              
Out[4]: <User: fatih>

In [5]: user = User.objects.filter(username='fatih').first()                                       

In [6]: user                                                                                       
Out[6]: <User: fatih>

In [7]: post_2 = Post(tittle='Blog 2' , content =' second post '  , author_id=user.id)             

In [8]: post_2.save()                                                                              

In [9]: Post.objects.all()                                                                         
Out[9]: <QuerySet [<Post: Post object (1)>, <Post: Post object (2)>]>

In [19]: post.author                                                                               
Out[19]: <User: fatih>

In [20]: post.author.email                                                                         
Out[20]: 'fatih.kgokmen@gmail.com'

In [21]: user                                                                                      
Out[21]: <User: fatih>

In [22]:                                                                                           

In [22]: user.post_set                                                                             
Out[22]: <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager at 0x7f878fd9c6d0>

In [23]: user.post_set.all()                                                                       
Out[23]: <QuerySet [<Post: Post object (1)>, <Post: Post object (2)>]>



In [22]: user.post_set                                                                             
Out[22]: <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager at 0x7f878fd9c6d0>

In [23]: user.post_set.all()                                                                       
Out[23]: <QuerySet [<Post: Post object (1)>, <Post: Post object (2)>]>

In [24]: user.post_set.create(tittle='Blog 3', content= 'Third Post ')                             
Out[24]: <Post: Post object (3)>

In [25]:  Post.object.all()                                                                        
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-25-9d1da07d3c7e> in <module>
----> 1 Post.object.all()

AttributeError: type object 'Post' has no attribute 'object'

In [26]:  Post.objects.all()                                                                       
Out[26]: <QuerySet [<Post: Post object (1)>, <Post: Post object (2)>, <Post: Post object (3)>]>