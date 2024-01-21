# Blog website made using Django and MySQL

This is a Django blog website made from scratch. Django has been deployed on Render.(Deployment on vercel doesnt work due to python version mismatch). MySQL has been hosted on aiven.

The features of the app are-
- Sign up user
- login user
- logout user
- create blog posts
- update blog posts
- delete blog posts
- like/unlike blog posts
- comment and nested comment on blog posts (can be made better)
- pagination for viewing blog posts

The different models in this app are-
- blog model
- like model
- comment model
For users, in built django auth model is used to save time

To run the server locally-
1. Create a virtual env by-
```
- pip install virtualenv
- python -m virtualenv venv
- venv/scripts/activate
```
2. Clone the repository in the root folder
3. Install all the requirements using requirement.txt
4. Run the migrations and migrate-
```
-python manage.py makemigrations
-python manage.py migrate
```
5. Run server
```
-python manage.py runserver
```

This will shoot up a local instance which will be connected to aiven's instance of mysql. To connect to a local db, just change the database params.


