# Full Stack Django Project

This is a **Full-Stack web application** built using the Django framework.  
The project follows the **MVC (Model–View–Controller)** pattern (implemented as MVT in Django), providing a scalable, secure, and maintainable foundation for web development.

---

## 🚀 Features

- **Database Models**  
  Structured models using Django ORM with migrations.

- **Dynamic Views & Templates**  
  Server-side rendering with Django template language.

- **Frontend Integration**  
  HTML, CSS, JavaScript, and Bootstrap for responsive UI.

- **Admin Dashboard**  
  Manage users, content, and data via Django’s built-in admin panel.

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML5, CSS3, Bootstrap, JavaScript  
- **Database:** SQLite (default) / PostgreSQL / 
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure

```bash
Full-Stack-Django-project/
│
├── first/          # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── blog/              # Example Django app
│   ├── models.py          # Database models
│   ├── views.py           # Application logic
│   ├── urls.py            # App-specific routes
│   └── templates/         # HTML templates
│
├── static/                # CSS, JS, images
├── templates/             # Shared templates (base.html, etc.)
├── manage.py
└── requirements.txt
