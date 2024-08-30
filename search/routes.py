import json
import os, sys
from flask import render_template, Blueprint, request
from flask_login import login_required

from config import Config
from myutils import open_json




Search = Blueprint('search', __name__, template_folder='templates', static_folder='static')

@Search.route("/search", methods=['GET','POST'])
@login_required
def search():
    
    return render_template('search.html', title='Search')