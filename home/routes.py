import json
import os, sys
from flask import render_template, Blueprint, request
from flask_login import login_required

from config import Config
from myutils import open_json




Home = Blueprint('home', __name__, template_folder='templates', static_folder='static')

@Home.route("/home", methods=['GET','POST'])
@login_required
def home():
    
    return render_template('home.html', title='Home')