# [![Pinolero Media](https://cloud.githubusercontent.com/assets/4844997/9451171/3ba44648-4a6a-11e5-8ddb-9a1438b1bb72.png)](http://pinoleromedia.com)

## Overview
A django base project template including bower and gulp initial configurations it is based on the [Django Project Template](https://github.com/LRPalacios/django-project-template)
This template includes a some inital apps and models that we have found common in web sites

[Django documentation on project template](https://docs.djangoproject.com/en/1.8/ref/django-admin/#startproject-projectname-destination).

## Requirements
1. Django > 1.8 
2. Node.js
3. Bower

## Setup
1. Create your virtualenv and activate it
2. Install django via `pip install django`
3. Create an empty directory for your project and enter **mkdir your_project_name** and **cd your_project_name**
4. Start your project using this template  
  **django 1.8 or higher use**  
``django-admin startproject --template https://github.com/PinoleroMedia/base-django-cms-template/zipball/master your_project_name .``  
The "." is so that you wont get an extra directory level (You could also use the comand without the "." at the end but make sure to skip the step where you create an empty directory)
5. *Optional* I recommend you first update your bower.json and package.json this is not necessary but it would be good for the documentation of your project.
6. Get into the directory where the project.json and bower.json are and do a **npm install** this will install all the node modules that the gulp tasks need.
