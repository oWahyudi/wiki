# Wiki - Django
Experimental - Web development using Django framework


1. Create virtual environment
   >python3 -m venv django-env

2. Activate virtual environment
   >source django-env/bin/activate

3. Install requirement
   >pip install -r requirement.txt

4. Create Django Project
   >django-admin startproject <PROJECT_NAME>

5. Run Django application (webserver)
   > python manage.py runserver (default port 8000)  
   > python manage.py runserver 8001  (run at port 8001)  

6. Create Django apps
   > stop webserver (CTR-C)  
   > python manage.py startapp <appname>  
   > Configure <appname> into INSTALL_APP in setting.py (in Django admin Project folder)  
   > Create urls.py in <appname> folder  
   > Configure <appname> path into URLPATTERN in urls.py (in Django admin project folder)  

7. Create default Session table.
   > python manage.py migrate (in Django admin project root folder)
