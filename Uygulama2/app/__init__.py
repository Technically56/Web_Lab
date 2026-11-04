from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['WTF_CSRF_ENABLED'] = False 
from app import routes
