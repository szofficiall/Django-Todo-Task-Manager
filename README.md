# 📝 Django Todo Task Manager

![Django](https://img.shields.io/badge/Django-6.x-092E20?style=for-the-badge\&logo=django\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.x-7952B3?style=for-the-badge\&logo=bootstrap\&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge\&logo=sqlite\&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge\&logo=html5\&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=for-the-badge\&logo=git\&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge\&logo=github\&logoColor=white)

---

## 📌 Project Title

# Django Todo Task Manager

A complete and responsive **Todo Task Management Application** built with **Python, Django, SQLite, HTML5, and Bootstrap 5**.

This project is designed to demonstrate the fundamentals of Django web development by implementing a complete **CRUD-based task management system**.

Users can create tasks, view all tasks, update existing tasks, delete tasks, and toggle tasks between **Pending** and **Completed** states.

The project also demonstrates important Django concepts such as:

* Django Models
* Django ORM
* Function-Based Views
* URL Routing
* URL Namespaces
* Django Templates
* Template Inheritance
* CSRF Protection
* Django Messages Framework
* Form Handling
* Database Migrations
* Bootstrap Integration
* Git & GitHub

---

# 👨‍💻 Developer

## Sultan Zaib

**Software Engineer | Python Developer | Django Developer**

This project was developed by **Sultan Zaib** as a practical Django project for learning, practicing, and demonstrating backend web development concepts.

> Built with ❤️ by **Sultan Zaib**

---

# 📖 About The Project

The Django Todo Task Manager is a simple but complete task management application.

The main purpose of this project is to understand how a Django application works from the database layer to the frontend.

The application follows the basic Django architecture:

```text
User
  ↓
URL
  ↓
View
  ↓
Model / Database
  ↓
Template
  ↓
HTML Response
  ↓
User
```

The project provides a clean Bootstrap-based interface where users can easily manage their daily tasks.

---

# ✨ Features

## 📋 Task Management

The application provides complete task management functionality.

### Create Task

Users can create a new task by entering:

* Task title
* Task description

---

### View Tasks

All tasks are displayed in a responsive Bootstrap table.

The task list displays:

* Serial number
* Title
* Description
* Completion status
* Creation date
* Available actions

---

### Update Task

Existing tasks can be edited.

Users can update:

* Task title
* Task description
* Completion status

---

### Delete Task

Users can delete tasks through a confirmation page.

A confirmation screen is displayed before the task is permanently removed from the database.

---

### Toggle Completion

Each task has a completion status.

A task can be:

```text
Pending
Completed
```

The status can be changed directly from the task list.

---

### 🔔 Django Messages

The project uses Django's built-in messages framework.

Users receive feedback after performing actions.

Examples:

```text
Task created successfully.
Task updated successfully.
Task deleted successfully.
Task marked as completed.
Task marked as pending.
Title cannot be empty.
```

---

### 🛡️ CSRF Protection

All POST forms use Django's CSRF protection:

```django
{% csrf_token %}
```

This helps protect forms against Cross-Site Request Forgery attacks.

---

### 📱 Responsive Interface

Bootstrap 5 is used to create a responsive interface.

The application can be used on:

* Desktop
* Laptop
* Tablet
* Mobile devices

---

# 🛠️ Technologies Used

| Technology       | Purpose                      |
| ---------------- | ---------------------------- |
| Python           | Backend programming language |
| Django           | Web framework                |
| SQLite           | Database                     |
| HTML5            | Page structure               |
| Bootstrap 5      | UI and responsive design     |
| Django Templates | Dynamic frontend             |
| Django ORM       | Database interaction         |
| Django Messages  | User notifications           |
| Git              | Version control              |
| GitHub           | Source code hosting          |
| VS Code          | Development environment      |

---

# 🧠 Django Concepts Covered

This project covers the following Django topics.

## 1. Django Project Structure

Understanding:

```text
Project
 ├── settings.py
 ├── urls.py
 ├── asgi.py
 └── wsgi.py
```

---

## 2. Django Application

The project contains a `todo` application.

The app contains:

```text
models.py
views.py
urls.py
admin.py
apps.py
```

---

## 3. Django Models

The project uses a `Task` model.

Example:

```python
class Task(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(
        blank=True,
        null=True
    )

    completed = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title
```

---

# 🗄️ Database Fields

The `Task` model contains the following fields:

| Field         | Type          | Purpose                       |
| ------------- | ------------- | ----------------------------- |
| `title`       | CharField     | Stores task title             |
| `description` | TextField     | Stores task description       |
| `completed`   | BooleanField  | Stores task completion status |
| `created_at`  | DateTimeField | Stores task creation time     |
| `updated_at`  | DateTimeField | Stores last update time       |

---

# 🔄 CRUD Operations

CRUD stands for:

```text
C → Create
R → Read
U → Update
D → Delete
```

This project implements all four operations.

| Operation | View                     |
| --------- | ------------------------ |
| Create    | `task_create()`          |
| Read      | `task_list()`            |
| Update    | `task_update()`          |
| Delete    | `task_delete()`          |
| Toggle    | `task_toggle_complete()` |

---

# 🔗 URL Routing

The Todo application uses:

```python
app_name = "todo"
```

This creates the `todo` namespace.

Routes:

| URL             | View                   | Name                   | Method     |
| --------------- | ---------------------- | ---------------------- | ---------- |
| `/`             | `task_list`            | `task_list`            | GET        |
| `/add/`         | `task_create`          | `task_create`          | GET / POST |
| `/edit/<id>/`   | `task_update`          | `task_update`          | GET / POST |
| `/delete/<id>/` | `task_delete`          | `task_delete`          | GET / POST |
| `/toggle/<id>/` | `task_toggle_complete` | `task_toggle_complete` | POST       |

---

# 🔐 URL Namespaces

Instead of using URLs directly, templates use Django's named URLs.

Example:

```django
{% url 'todo:task_list' %}
```

Create task:

```django
{% url 'todo:task_create' %}
```

Update task:

```django
{% url 'todo:task_update' task.id %}
```

Delete task:

```django
{% url 'todo:task_delete' task.id %}
```

Toggle completion:

```django
{% url 'todo:task_toggle_complete' task.id %}
```

This makes the application easier to maintain.

---

# 👁️ Views

The application uses Function-Based Views.

## Task List

```python
def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")

    return render(
        request,
        "todo/task_list.html",
        {"tasks": tasks}
    )
```

This retrieves all tasks from the database and displays them.

---

## Create Task

```python
def task_create(request):
```

This view handles:

* GET request
* POST request
* Title validation
* Task creation
* Success messages

---

## Update Task

```python
def task_update(request, id):
```

This view:

1. Retrieves the task
2. Displays the edit form
3. Accepts updated data
4. Validates the title
5. Saves changes
6. Redirects to the task list

---

## Delete Task

```python
def task_delete(request, id):
```

This view:

1. Retrieves the task
2. Displays confirmation
3. Deletes the task after POST
4. Redirects to task list

---

## Toggle Task

```python
def task_toggle_complete(request, id):
```

This changes:

```text
Pending → Completed
```

or:

```text
Completed → Pending
```

---

# 📂 Complete Project Folder Structure

```text
Django-Todo-Task-Manager/
│
├── manage.py
│
├── db.sqlite3
│
├── requirements.txt
│
├── README.md
│
├── .gitignore
│
│
├── todo/
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   │
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
│
│
├── project/
│   │
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
│
├── templates/
│   │
│   └── todo/
│       │
│       ├── base.html
│       ├── task_list.html
│       ├── task_form.html
│       └── task_confirm_delete.html

> `project/` ko apne actual Django project folder ke naam se replace karna.

---

# 📁 Folder & File Explanation

## `manage.py`

Django project ka command-line utility hai.

Isse hum commands run karte hain:

```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py test
```

---

# 📁 `todo/`

Ye application ka main folder hai.

Isme Todo application ki complete functionality hoti hai.

---

## `todo/models.py`

Database structure define karta hai.

Example:

```python
class Task(models.Model):
```

---

## `todo/views.py`

Application ki business logic handle karta hai.

Main views:

```text
task_list
task_create
task_update
task_delete
task_toggle_complete
```

---

## `todo/urls.py`

Application ke URLs define karta hai.

Example:

```python
path("", views.task_list, name="task_list")
```

---

## `todo/admin.py`

Django Admin configuration ke liye use hota hai.

---

## `todo/apps.py`

Django application configuration contain karta hai.

---

## `todo/migrations/`

Database changes ko track karta hai.

Example:

```text
0001_initial.py
```

---

# 📁 `templates/todo/`

Frontend HTML templates yahan rakhe gaye hain.

---

## `base.html`

Common layout contain karta hai.

Isme:

* Navbar
* Bootstrap CSS
* Bootstrap JavaScript
* Messages
* Template blocks

included hain.

Other templates `base.html` ko extend karte hain.

---

## `task_list.html`

All tasks display karta hai.

Is page par:

* Tasks
* Status
* Edit button
* Delete button
* Toggle button

available hain.

---

## `task_form.html`

Create aur update dono ke liye use hota hai.

---

## `task_confirm_delete.html`

Task delete karne se pehle confirmation show karta hai.

---

# 🗃️ Database

Development ke liye project mein **SQLite** use kiya gaya hai.

Database file:

```text
db.sqlite3
```

Django ORM database operations handle karta hai.

Example:

```python
Task.objects.all()
```

---

# 🔎 ORM Query

Tasks ko latest created task ke order mein retrieve kiya jata hai:

```python
Task.objects.all().order_by("-created_at")
```

Individual task retrieve karne ke liye:

```python
get_object_or_404(Task, id=id)
```

use kiya gaya hai.

---

# 🔄 Application Workflow

```text
                    ┌──────────────────┐
                    │    User Opens    │
                    │    Todo App      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Task List     │
                    └────────┬─────────┘
                             │
             ┌───────────────┼────────────────┐
             │               │                │
             ▼               ▼                ▼
        Create Task      Edit Task       Delete Task
             │               │                │
             ▼               ▼                ▼
        Save to DB       Update DB        Delete from DB
             │               │                │
             └───────────────┼────────────────┘
                             │
                             ▼
                     Toggle Completion
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
                Completed          Pending
```

---


# ⚙️ Installation

Follow the steps below to run this project locally.

---

## 1. Clone Repository

```bash
git clone https://github.com/szofficiall/Django-Todo-Task-Manager.git
```

---

## 2. Enter Project Directory

```bash
cd Django-Todo-Task-Manager
```

---

## 3. Create Virtual Environment

Windows:

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows CMD

```bash
venv\Scripts\activate
```

### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements file does not exist:

```bash
pip install django
```

---

# 🗄️ Database Setup

Run:

```bash
python manage.py makemigrations
```

Then:

```bash
python manage.py migrate
```

---

# 👤 Create Admin User

Run:

```bash
python manage.py createsuperuser
```

Enter:

```text
Username
Email
Password
```

---

# ▶️ Run Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 🔐 Django Admin

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

Login using the superuser account.

---

# 🧪 Testing

Run Django tests:

```bash
python manage.py test
```

Testing can be extended for:

* Task creation
* Task update
* Task deletion
* Task completion
* Empty title validation
* URL responses
* Template rendering

---

# 🛡️ Security

The project uses Django's built-in security features.

### CSRF Protection

Forms include:

```django
{% csrf_token %}
```

### ORM Protection

Database operations use Django ORM instead of manually constructing SQL queries.

### POST Requests

State-changing operations such as delete and toggle are performed using POST requests.

---

# 📱 Responsive Design

Bootstrap 5 is used to create a responsive layout.

The application uses Bootstrap components such as:

```text
Navbar
Container
Table
Buttons
Forms
Cards
Alerts
Responsive Table
```

---

# 🔔 Message System

Django Messages Framework provides user feedback.

Example:

```python
messages.success(
    request,
    "Task created successfully."
)
```

Error message:

```python
messages.error(
    request,
    "Title cannot be empty."
)
```

Info message:

```python
messages.info(
    request,
    "Task marked as pending."
)
```

---

# 📦 Requirements

The main dependency is Django.

Example:

```text
Django
```

You can generate the complete environment dependency list using:

```bash
pip freeze > requirements.txt
```

---

# 🧹 `.gitignore`

The project should ignore unnecessary files.

Recommended:

```gitignore
__pycache__/
*.py[cod]

venv/
env/
.venv/

*.log

db.sqlite3

.env

.vscode/
.idea/

media/

.DS_Store
Thumbs.db
```

---

# 🌱 Git Workflow

Initialize Git:

```bash
git init
```

Check files:

```bash
git status
```

Add files:

```bash
git add .
```

Commit:

```bash
git commit -m "Initial commit - Django Todo Task Manager"
```

Rename branch:

```bash
git branch -M main
```

Add remote:

```bash
git remote add origin https://github.com/szofficiall/Django-Todo-Task-Manager.git
```

Push:

```bash
git push -u origin main
```

---

# 🔄 Future Updates

When making new changes:

```bash
git add .
git commit -m "Add new feature"
git push
```

---

# 🚀 Future Improvements

The current project can be expanded into a complete productivity platform.

## 🔐 Authentication

Possible future features:

* User Registration
* Login
* Logout
* Password Reset
* User Profiles

---

## 👤 User-Specific Tasks

Each user can have their own tasks.

```text
User A
 ├── Task 1
 ├── Task 2
 └── Task 3

User B
 ├── Task 1
 └── Task 2
```

---

## 🔎 Search

Add task search functionality:

```text
Search by title
Search by description
```

---

## 🏷️ Categories

Tasks can be organized into categories:

```text
Work
Personal
Study
Shopping
Programming
Other
```

---

## 🎯 Priority

Tasks can have priority levels:

```text
Low
Medium
High
Urgent
```

---

## 📅 Due Dates

Add:

```text
Due Date
Due Time
Deadline
```

---

## 📊 Dashboard

A future dashboard could display:

```text
Total Tasks
Completed Tasks
Pending Tasks
Overdue Tasks
Completion Percentage
```

---

## 🌙 Dark Mode

A dark mode can be added for better user experience.

---

## 📄 Pagination

Pagination can be added when the number of tasks becomes large.

---

## 🔎 Search & Filtering

Possible filters:

```text
All
Completed
Pending
High Priority
Overdue
```

---

## 🌐 REST API

The application can later be converted into an API using:

```text
Django REST Framework
```

Possible API endpoints:

```text
GET    /api/tasks/
POST   /api/tasks/
GET    /api/tasks/<id>/
PUT    /api/tasks/<id>/
DELETE /api/tasks/<id>/
```

---

# ☁️ Deployment

The application can be deployed to:

* Render
* Railway
* PythonAnywhere
* VPS
* AWS
* Azure
* Google Cloud

Before production deployment, configure:

```text
DEBUG = False
ALLOWED_HOSTS
SECRET_KEY
STATIC_FILES
DATABASE
HTTPS
```

Never expose your production secret key publicly.

---

# 🤝 Contributing

Contributions are welcome.

## Step 1

Fork this repository.

## Step 2

Clone your fork:

```bash
git clone https://github.com/szofficiall/Django-Todo-Task-Manager.git
```

## Step 3

Create a branch:

```bash
git checkout -b feature/new-feature
```

## Step 4

Make your changes.

## Step 5

Commit:

```bash
git add .
git commit -m "Add new feature"
```

## Step 6

Push:

```bash
git push origin feature/new-feature
```

## Step 7

Create a Pull Request.

---

# 📜 License

This project is intended for **educational and personal development purposes**.

You are free to:

* Study the source code
* Modify the project
* Improve the functionality
* Use it as a learning reference

If you use significant portions of this project in another public project, giving credit to the original developer is appreciated.

---

# ⭐ Support

If you found this project useful or helpful:

### ⭐ Star this repository

### 🍴 Fork this repository

### 💡 Suggest improvements

Your support helps motivate further development.

---

# 📚 Learning Resources

While developing this project, the following concepts are especially important to understand:

```text
Python
   ↓
Django
   ↓
Models
   ↓
ORM
   ↓
Views
   ↓
URLs
   ↓
Templates
   ↓
Forms
   ↓
Database
   ↓
CRUD
```

---

# 🎯 Project Goals

The main goals of this project are:

* Learn Django fundamentals
* Understand CRUD operations
* Practice Django ORM
* Understand URL routing
* Practice template inheritance
* Learn form handling
* Work with SQLite
* Use Bootstrap with Django
* Understand CSRF protection
* Use Django Messages
* Practice Git and GitHub
* Build a real-world Django project

---

# 🏆 Project Highlights

```text
✅ Django Based
✅ Complete CRUD
✅ SQLite Database
✅ Bootstrap 5 UI
✅ Responsive Design
✅ Django ORM
✅ URL Namespaces
✅ CSRF Protection
✅ Django Messages
✅ Form Validation
✅ Task Completion Toggle
✅ Delete Confirmation
✅ Template Inheritance
✅ GitHub Ready
```

---

# 🧑‍💻 About the Developer

## Sultan Zaib

I am **Sultan Zaib**, a Software Engineer and Django/Python developer focused on building practical web applications and continuously improving my backend development skills.

This Todo Task Manager is part of my Django development journey and demonstrates my understanding of:

* Python
* Django
* Database Design
* Django ORM
* CRUD Applications
* HTML
* Bootstrap
* Git
* GitHub

---

# 💙 Final Note

Thank you for visiting this project!

If you are learning Django, this project can serve as a simple starting point for understanding how a complete CRUD application works.

The project can be extended into a much larger task management platform by adding authentication, user-specific tasks, categories, priorities, deadlines, notifications, dashboards, APIs, and deployment.

---

# ⭐ Django Todo Task Manager

### Built with ❤️ by Sultan Zaib

**Python • Django • Bootstrap • SQLite • Git • GitHub**

---

## 👨‍💻 Developer

**Sultan Zaib**

> Software Engineer | Python Developer | Django Developer

⭐ If you like this project, don't forget to **Star the Repository**!
