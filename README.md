# 📝 Todo List API with Django REST Framework

A collaborative Todo List RESTful API built with Django & Django REST Framework.  
This project was developed as a team effort and supports user authentication using JWT, allows users to manage todo lists and tasks, and includes advanced features like pagination, throttling, CORS, and search capabilities.

---

## 🔐 Authentication (Simple JWT)

- **POST** `/auth/register`: Register a new user.
- **POST** `/auth/profile`: Get logged-in user's profile (username + total task count).
- **POST** `/auth/api/token/`: Obtain JWT token (login).
- **POST** `/auth/api/token/refresh/`: Refresh access token.
- **POST** `/auth/api/token/verify/`: Verify token validity.

---

## 📂 Todo Lists

- **GET** `   /lists`: Retrieve all lists (paginated).
- **GET** `   /lists/<id>`: Retrieve a specific list.
- **POST** `  /lists`: Create a new list.
- **PUT** `   /lists/<id>`: Update an existing list.
- **DELETE** `/lists/<id>`: Delete a list.
- **GET** `   /lists/search`: Search lists by title.

---

## ✅ Todo Tasks (Per List)

- **GET** `   /lists/<list_id>/tasks`: Get all tasks in a list.
- **GET** `   /lists/<list_id>/tasks/<task_id>`: Get a single task.
- **POST** `  /lists/<list_id>/tasks`: Create a task in a list.
- **PUT** `   /lists/<list_id>/tasks/<task_id>`: Update a task.
- **DELETE** `/lists/<list_id>/tasks/<task_id>`: Delete a task.
- **PATCH** ` /lists/<list_id>/tasks/<task_id>/complete`: Mark a task as completed.
- **GET** `   /tasks/search`: Search tasks by name.

---

## ⚙️ Features

- 🔐 Authentication using **Simple JWT**
- 🧾 Full **CRUD** for Todo Lists and Tasks
- ✅ Mark tasks as completed (disappear from views)
- 📄 **Pagination** support for list/task views
- ⏱️ **Throttling** enabled to protect the API
- 🌐 **CORS** enabled for frontend integration
- 🔍 Search functionality:
  - Search lists by **title**
  - Search tasks by **name**
- 📘 **Swagger UI** documentation
