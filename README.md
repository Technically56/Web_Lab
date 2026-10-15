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
└── LICENSE                 # MIT License
```

### Modules Overview

- **`Ders1`**: Introduction to basic Flask web development concepts:
  - Modular application factory structure (`app/` package)
  - Routing and dynamic URL parameters (`/`, `/index`, `/<username>`)
  - Jinja2 template inheritance (`base.html`) and view rendering (`index.html`)

- **`Uygulama1`**: A simple library book management practice:
  - Passing structured collections (book records) to Jinja2 templates
  - Conditional rendering (reading status check)
  - Template navigation and URL generation (`url_for`)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Flask

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
   pip install flask
   ```

---

## 💻 Running the Projects

Each directory is a standalone Flask application.

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

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
