# Job Application Tracker

A full-stack web application for tracking job applications through the hiring process. Built with Django 6.0.3 as the third project in a structured backend development portfolio, following a Recipe Manager API and a Movie Watchlist API built with FastAPI.

---

## Live Demo

[View the live app](https://your-render-url.onrender.com/applications/)

---

## Features

- User registration and session-based authentication
- Create, read, update, and delete job applications
- Track company name, job title, date applied, application status, and notes
- Application status managed via predefined choices (Applied, Interviewing, Offered, Rejected)
- All views restricted to authenticated users
- Users can only access and modify their own applications
- Form validation including required fields, date format enforcement, and character limits

---

## Tech Stack

- **Framework:** Django 6.0.3
- **Database:** SQLite
- **Authentication:** Django built-in session-based auth
- **Language:** Python 3

---

## Technical Decisions

**Django over FastAPI:** My previous two portfolio projects were built with FastAPI. I chose Django for this project to expand my skillset and deepen my understanding of how backend development flows in a batteries-included framework.

**Class-based views over function-based views:** Django's generic class-based views (ListView, CreateView, UpdateView, DeleteView) allow for reusability of common logic and reduce boilerplate. Using CBVs also demonstrates familiarity with Django's built-in patterns.

**Session-based auth over JWT:** Django's built-in session-based authentication was chosen for its simplified implementation and server-side state management, which is well suited to a server-rendered web application as opposed to a decoupled API.

---

## Project Structure

```
ApplicationTracker/
├── config/                  # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── applications/            # Main app
│   ├── models.py            # JobApplication model
│   ├── views.py             # Class-based views
│   ├── forms.py             # JobApplicationForm with validation
│   ├── urls.py              # App URL routing
│   ├── admin.py             # Admin registration
│   └── templates/
│       └── applications/
│           ├── jobapplication_list.html
│           ├── jobapplication_form.html
│           └── jobapplication_confirm_delete.html
├── templates/
│   └── registration/
│       ├── login.html
│       └── register.html
└── manage.py
```

---

## Setup and Installation

### Prerequisites

- Python 3.10+
- Git

### Steps

1. **Clone the repository**

```bash
git clone https://github.com/Aberlinghoff/ApplicationTracker
cd ApplicationTracker
```

2. **Create and activate a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install django
```

4. **Apply migrations**

```bash
python3 manage.py migrate
```

5. **Create a superuser (optional)**

```bash
python3 manage.py createsuperuser
```

6. **Run the development server**

```bash
python3 manage.py runserver
```

7. **Open in your browser**

Navigate to `http://127.0.0.1:8000/` and register an account to get started.

---

## Usage

- Register a new account or log in with an existing one
- From the application list, click **Track New Application** to add a new job application
- Use the **Update** and **Delete** buttons next to each application to manage your entries
- Log out when finished using the logout link

---

## Other Projects in This Portfolio

- [Recipe Manager API](https://github.com/Aberlinghoff) — FastAPI, SQLAlchemy, SQLite, full CRUD
- [Movie Watchlist API](https://github.com/Aberlinghoff) — FastAPI, SQLAlchemy, JWT authentication, TMDB external API integration
