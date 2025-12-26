# Blog App (Django)

A simple CRUD blog application built with Django  created to practice backend development. It provides the usual blog features (create, read, update, delete posts) and a minimal admin interface. Design and frontend contributions are very welcome!

## Features
- Create, read, update, delete (CRUD) posts
- Simple, minimal codebase intended for learning backend concepts
- Ready for frontend/design improvements

## Tech
- Python (Django)
- SQLite (default) replaceable with any Django-supported database
- (Add any additional libs in `requirements.txt`)

## Prerequisites
- Python 3.8+
- pip
- (optional) virtualenv or venv

## Quick start

1. Clone the repository
```bash
git clone https://github.com/GradienNinja/Blog-App.git
cd Blog-App
```

2. Create and activate a virtual environment
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Apply migrations and create a superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

5. (Optional) Add environment variables
- If the project uses `.env`, create `.env` from `.env.sample` and set `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, etc.

6. Run the development server
```bash
python manage.py runserver
```
Open http://127.0.0.1:8000/ to view the site. Visit `/admin` to manage posts via the Django admin.



## Deployment
This project is suitable for simple deployment. For production, set `DEBUG = False`, configure `ALLOWED_HOSTS`, use a production database, and serve static files (e.g., with WhiteNoise) or via a proper web server (NGINX/Gunicorn).

## Contributing
Contributions are welcome  especially design and frontend improvements!
 Open an issue to discuss big changes or design proposals.
Submit a pull request for bug fixes, features, or UI/UX improvements.
If you want to help with design, feel free to add sketches, a new template, or a CSS framework integration.

