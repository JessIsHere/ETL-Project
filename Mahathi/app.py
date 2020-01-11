#importing dependencies for flask module

from flask import Flask,jsonify

#importing dependencies for Database in the back end

import sqlalchemy
from sqlalchemy import create_engine,func
from sqlalchemy.orm import session



#Flask Setup

app = Flask(__name__)


#Flask routes