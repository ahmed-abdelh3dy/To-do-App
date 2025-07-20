# 📝 Todo List API with Django REST Framework

A fully functional Todo List RESTful API built with Django & Django REST Framework. This project supports user authentication using JWT, allows users to manage todo lists and tasks, includes advanced features like pagination, throttling, CORS, and search capabilities.

---

## 🔐 Authentication (Simple JWT)

- **POST** `/auth/register`: Register a new user.
- **POST** `/auth/login`: Obtain JWT token.
- **POST** `/auth/profile`: Get logged-in user's profile (username + total task count).

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

- 🔐 JWT Authentication using Simple JWT
- 📋 Full CRUD for Todo Lists and Tasks
- ✅ Task completion logic (completed tasks are hidden from all views)
- 🔍 Search endpoint for lists and tasks
- 🌐 CORS enabled
- ⏳ Throttling enabled
- 📄 Pagination enabled
