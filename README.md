# django-blog-app-rest

A django web app integrated with rest framework.

## API Endpoints
# For User Model
- [POST] *localhost:8000/api/users-model/login/* **returns a token which is to be used with every request to the server** (username and password to be provided in form data)
- [GET] *localhost:8000/api/users-model/user/* **returns the list of all the users on the blog**
- [GET] *localhost:8000/api/users-model/user/<pk>/* **returns the user associated with that primary key(pk)**
- [PUT] *localhost:8000/api/users-model/user/<pk>/* **edit the information of the user associated with that primary key(pk)** (any information to be edited should be specified in the json object similar to the get one (only specify the fields you wanna change))
# For Post Model
- [GET] *localhost:8000/api/post-model/post/* **returns all the posts on the blog**
- [GET] *localhost:8000/api/post-model/<username>/posts/* **returns all the posts by the user with <username>**
- [GET] *localhost:8000/api/post-model/post/<pk>/* **returns the post with <pk>**
- [GET] *localhost:8000/api/post-model/post/<pk>/* **edit the post with <pk>**