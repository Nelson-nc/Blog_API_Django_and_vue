# Blog API

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=fff)](#)
[![DRF](https://img.shields.io/badge/Django%20Rest%20Framework-ff1709?logo=django&logoColor=white)](#)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=fff)](#)

A backend API for a blog application, providing user authentication and blog post management features.

## Features
- **User Authentication**: Secure user registration and login using JWT (JSON Web Tokens).
- **Blog Management**: Create, read, update, and delete blog posts.
- **Profile Management**: User profile handling.

## Usage
Run the development server:
```sh
cd Blog_backend
python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/`.

## Installation/Setup
<p>First you must have [Python](https://www.python.org) installed.</p>

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd BLOG_API/Blog_backend
   ```

2. **Install dependencies:**
   ```sh
   pip install django
   pip install djangorestframework
   pip install djangorestframework-simplejwt
   pip install django-cors-headers
   ```

3. **Database Setup:**
   Run migrations to set up the SQLite database:
   ```sh
   python manage.py migrate
   ```

4. **Create a Superuser (Optional):**
   To access the Django Admin interface:
   ```sh
   python manage.py createsuperuser
   ```

## Future Ideas
- Add comment functionality for posts.
- Implement post categories and tagging.
- Add pagination for post lists.

## How to contribute
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make changes and test thoroughly.
- Submit a pull request with a clear description of your changes.
