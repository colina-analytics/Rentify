import json
import os, sys
from flask import render_template, Blueprint, request
from flask_login import login_required

from config import Config
from myutils import open_json




Messaging = Blueprint('messaging', __name__, template_folder='templates', static_folder='static')

@Messaging.route("/messaging", methods=['GET','POST'])
@login_required
def messaging():
    
    return render_template('messaging.html', title='Messaging')