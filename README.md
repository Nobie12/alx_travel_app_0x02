# alxtravelapp

A real-world **Django** application serving as the foundation for a travel listing platform.  
This milestone focuses on setting up the initial project structure, configuring a robust database, and integrating tools for **API documentation** and **maintainable configurations**.  
The goal is to equip developers with **industry-standard best practices** for starting and managing Django-based projects efficiently.

---

## 🚀 About the Project

`alxtravelapp` is the backend for a travel listings platform.  
In this milestone, you will:

- Set up a **scalable Django backend**.
- Integrate **MySQL** for database management.
- Use **Swagger** for automated API documentation.
- Manage settings securely with **django-environ**.
- Prepare the codebase for **future features** and **team collaboration**.

---

## 🎯 Learning Objectives

By completing this milestone, you will:

### 1. Master Advanced Project Initialization
- Bootstrap Django projects with **modular, production-ready configurations**.
- Employ **environment variable management** for secure and scalable settings.

### 2. Integrate Key Developer Tools
- Set up and use **Swagger** (`drf-yasg`) for API documentation.
- Implement **CORS headers** and **MySQL configurations** for robust API interactions.

### 3. Collaborate Effectively Using Git
- Structure your project for **team collaboration** with a version-controlled setup.

### 4. Adopt Industry Best Practices
- Manage dependencies, database configurations, and application structure in a maintainable way.

---

## 📋 Requirements

Before starting, make sure you have:

- **Django** and **Django REST Framework** knowledge.
- Understanding of **MySQL** and database management.
- Familiarity with **Git** and version control.
- A basic grasp of **django-environ** for environment variables.

---

## 🛠️ Key Highlights

### **1. Project Initialization**
- Create a Django project named `alxtravelapp`.
- Add an app named `listings` to encapsulate core functionalities.

### **2. Dependency Management**
Installed packages include:
- `django` – Core framework.
- `djangorestframework` – REST API support.
- `django-cors-headers` – Cross-Origin Resource Sharing setup.
- `drf-yasg` – Swagger API documentation.
- `celery` + `rabbitmq` – Future background task support.

### **3. Settings Configuration**
- **django-environ** to securely handle environment variables.
- **MySQL** as the primary database in `settings.py`.
- REST Framework + CORS headers configured for API support.

### **4. Swagger Integration**
- Automatic API documentation via Swagger UI.
- Accessible at: `http://localhost:8000/swagger/`

### **5. Version Control**
- Git repository initialized and structured for collaboration.
- Code pushed to a public GitHub repo named **`alxtravelapp`**.

---

## 📦 Installation & Setup

1️⃣ **Clone the repository**
```bash
git clone https://github.com/<your-username>/alxtravelapp.git
cd alxtravelapp
```

2️⃣ **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3️⃣ **Install dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Set up .env file**
```bash
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=mysql://user:password@localhost:3306/db_name
ALLOWED_HOSTS=127.0.0.1,localhost
```

5️⃣ **Run migrations**
```bash
python manage.py migrate
```

6️⃣ **Start the development server**
```bash
python manage.py runserver
```

> Swagger docs will be available at:

```arduino
http://127.0.0.1:8000/swagger/
```

## 👥 Authors
Ken Aule