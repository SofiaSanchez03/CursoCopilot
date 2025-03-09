from flask import Flask

app = Flask(__name__)

from app.controllers import *
from app.models import *
from app.views import *