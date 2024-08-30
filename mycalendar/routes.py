import json
import os, sys
from flask import render_template, Blueprint, request
from flask_login import login_required

from config import Config
from myutils import open_json



MyCalendar = Blueprint('calendar', __name__, template_folder='templates', static_folder='static')

@MyCalendar.route("/calendar", methods=['GET','POST'])
@login_required
def calendar():
    
    return render_template('calendar.html', title='Calendar')