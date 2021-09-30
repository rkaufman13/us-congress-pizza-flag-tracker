from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_migrate import Migrate
from flask_cors import CORS
from flask_qrcode import QRcode
import os
import qrcode

app = Flask(__name__)
qrcode = QRcode(app)

CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.config["FRONTEND_URI"] = os.environ["FRONTEND_URI"]
app.config["SECRET_KEY"] = "0846b992676081f8785b3012c380097d"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from init_db import init_app
init_app(app)

migrate = Migrate(app, db)
app.secret_key = "the#flag#app#key"
