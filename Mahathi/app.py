# Import dependencies for python flask module

from flask import Flask, jsonify
import json

#importing dependencies from sqlalchemy to connect to DataBase in the back end

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#importing dependencies for python
import numpy as np
import os



######################
# Database Setup
######################

pg_user = 'postgres'
pg_password = 'Dhanista#4'
db_name = 'ETL-Project'

connection_string = f"{pg_user}:{pg_password}@localhost:5433/{db_name}"
engine = create_engine(f'postgresql://{connection_string}')


# reflect an existing database into a new model

Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table

Income = Base.classes.country_income 
traffiking_details = Base.classes.global_traffiking
Countries = Base.classes.countries


######################
# Flask Setup
######################

app = Flask(__name__)


# Define route to homepage

@app.route("/")
def home():
        return (f"Welcome to Our Home Page<br/><br/>"
                f"Available Routes:<br/><br/>"
                f"/api/v1.0/income<br/>" 
                f"/api/v1.0/country-codes<br/>"
                f"/api/v1.0/ages<br/>"
                f"/api/v1.0/years<br/>"
                f"/api/v1.0/gender<br/><br/>")
                

@app.route("/api/v1.0/ages")
def age():
    """Age Ranges"""


    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Query unique age ranges
    age = session.query(traffiking_details.Age_Range).distinct().all()

    session.close()

    agerange_list = list(np.ravel(age))

    
    return jsonify(agerange_list)


@app.route("/api/v1.0/years")
def years():
    """Years"""


    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Query distinct years from main table
    year = session.query(traffiking_details.Year_Identified).distinct().order_by(traffiking_details.Year_Identified).all()

    session.close()

    year_list = str(np.ravel(year))

    
    return jsonify(year_list)


@app.route("/api/v1.0/gender")
def gender():
    """Gender"""
    session = Session(engine)

    # gender count

    gen = session.query(traffiking_details.Gender,func.count(traffiking_details.Gender).label('count')).group_by(traffiking_details.Gender).all()

    session.close()

    gen_list = str(np.ravel(gen)) 

    return jsonify(gen_list)


# Routes for country codes and income

@app.route("/api/v1.0/income")
def income():
    """List of income levels"""
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Query the income level and country code from income table
    income = session.query(Income.countrycode, Income.incomelevel).all()

    #session.close()
    session.close()

    #return jsonify(income_list)

    income_list = []

    for country_income in income:
        income_dict = {}
        income_dict["Country-Code"] = country_income.countrycode
        income_dict["Income-Level"] = country_income.incomelevel
        income_list.append(income_dict)

    # return JSON list of incomes

    return(jsonify(income_list))
      

# Route for Country names and codes

@app.route("/api/v1.0/country-codes")
def country_list():
    """List of all countries with codes"""
    session = Session(engine)

    countries_query = session.query(Countries.country_name,Countries.country_code).all()

    session.close()

    country_list = []
    cou_code_list = []
    country_code_dict = {}

    for countries in countries_query:
        country_list.append(countries.country_name)
        cou_code_list.append(countries.country_code)
        country_code_dict = dict(zip(country_list,cou_code_list))

    return(jsonify(country_code_dict))

    

# Run in development mode
if __name__ == "__main__":
    app.run(debug=True)
