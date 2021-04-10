import functools
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
app = Flask(__name__, template_folder='Templates',instance_relative_config=True)
# app.config['SECRET_KEY'] = 'project'
app.secret_key = 'project'

app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'database.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# app.config.from_pyfile('config.py')
app.debug = True

db = SQLAlchemy(app)

bp = Blueprint('auth', __name__, url_prefix='/auth')