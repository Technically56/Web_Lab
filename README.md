# Web_Lab

Web programming laboratory exercises and practices built with Python and Flask.

## 📂 Project Structure

```text
Web_Lab/
├── Ders1/                  # Lesson 1: Introduction to Flask
│   ├── app/
│   │   ├── templates/      # Jinja2 templates (base.html, index.html)
│   │   ├── __init__.py     # Flask app initialization
│   │   └── routes.py       # Route handlers and URL parameter examples
│   └── web_lab.py          # Application entry point
├── Uygulama1/              # Practice 1: Library Application
│   ├── app/
│   │   ├── templates/      # Templates with inheritance and conditionals
│   │   ├── __init__.py     # Flask app initialization
│   │   └── routes.py       # Library routes and data passing
│   └── main.py             # Application entry point
├── Ders2/                  # Lesson 2: Web Forms
│   ├── app/
│   │   ├── templates/      # Login, forgot password and about pages
│   │   ├── __init__.py     # Flask app initialization
│   │   ├── forms.py        # Flask-WTF form classes
│   │   └── routes.py       # Page and form handling routes
│   ├── config.py           # Application configuration
│   └── web_lab.py          # Application entry point
├── Uygulama2/              # Practice 2: Login Feedback Form
│   ├── app/
│   │   ├── templates/      # Ders2 pages plus the feedback page
│   │   ├── __init__.py     # Flask app initialization
│   │   ├── feedback.txt    # Saved feedback submissions
│   │   ├── forms.py        # Ders2 forms plus the feedback form
│   │   └── routes.py       # Ders2 routes plus the feedback route
│   ├── config.py           # Application configuration
│   └── web_lab.py          # Application entry point
├── Ders3/                  # Lesson 3: Databases and Migrations
│   ├── app/
│   │   ├── templates/      # Pages carried over from Uygulama2
│   │   ├── __init__.py     # Flask app, database and migration setup
│   │   ├── forms.py        # Flask-WTF form classes
│   │   ├── models.py       # User and Post database models
│   │   └── routes.py       # Page and form handling routes
│   ├── migrations/         # Flask-Migrate migration scripts
│   ├── .flaskenv           # Sets FLASK_APP for the flask command
│   ├── config.py           # Application and database configuration
│   ├── populate_db.py      # Adds sample users and posts
│   └── web_lab.py          # Application entry point and flask shell setup
├── .gitignore              # Files left out of version control
├── requirements.txt        # Pinned Python dependencies
└── LICENSE                 # MIT License
```

### Modules Overview

- **`Ders1`**: Introduction to basic Flask web development concepts:
  - Package-based application structure (`app/` package)
  - Routing and dynamic URL parameters (`/`, `/index`, `/<username>`)
  - Jinja2 template inheritance (`base.html`) and view rendering (`index.html`)

- **`Uygulama1`**: A simple library book management practice:
  - Passing structured collections (book records) to Jinja2 templates
  - Conditional rendering (reading status check)
  - Template navigation and URL generation (`url_for`)

- **`Ders2`**: Builds on `Ders1` with web forms:
  - Application configuration through a `Config` class
  - Login and forgot password forms with Flask-WTF, including validation and CSRF protection
  - Flash messages and redirects after form submission

- **`Uygulama2`**: Builds on `Ders2` with a login feedback form:
  - A new form class with its own route and template
  - Saving submitted feedback to `app/feedback.txt`

- **`Ders3`**: Builds on `Uygulama2` with a database:
  - `User` and `Post` SQLAlchemy models with a one-to-many relationship, stored in SQLite
  - Schema migrations with Flask-Migrate (`flask db`)
  - Sample data from `populate_db.py`, with passwords stored as scrypt hashes
  - A `flask shell` setup that provides `sa`, `so`, `db`, `User` and `Post`

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Technically56/Web_Lab.git
   cd Web_Lab
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   # On Windows: .venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

`Ders2`, `Uygulama2` and `Ders3` read `SECRET_KEY` from the environment and fall back to a development value if it isn't set. Set your own value anywhere other than local development.

`Ders3` also reads `DATABASE_URL` from the environment and uses a SQLite file, `Ders3/app.db`, if it isn't set.

---

## 💻 Running the Projects

Each directory is a standalone Flask application. Run the commands below from the repository root.

### Run Ders 1

```bash
cd Ders1
flask --app web_lab run
```
Visit `http://127.0.0.1:5000/` or `http://127.0.0.1:5000/YourName` in your browser.

### Run Uygulama 1

```bash
cd Uygulama1
flask --app main run
```
Visit `http://127.0.0.1:5000/` or `http://127.0.0.1:5000/mylibrary` in your browser.

### Run Ders 2

```bash
cd Ders2
flask --app web_lab run
```
Visit `http://127.0.0.1:5000/login`, `http://127.0.0.1:5000/forget_password` or `http://127.0.0.1:5000/about` in your browser.

### Run Uygulama 2

```bash
cd Uygulama2
flask --app web_lab run
```
Visit `http://127.0.0.1:5000/login_feedback` in your browser.

### Run Ders 3

```bash
cd Ders3
flask db upgrade
python populate_db.py
flask run
```
`flask db upgrade` creates the database and its tables, and `populate_db.py` adds the sample data. You only need these two commands the first time.

Visit `http://127.0.0.1:5000/` in your browser, or use `flask shell` to work with the models directly:

```python
db.session.scalars(sa.select(User)).all()
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
