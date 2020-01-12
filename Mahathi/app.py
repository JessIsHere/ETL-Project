# Import dependencies for python flask module

from flask import Flask, jsonify

#importing dependencies from sqlalchemy to connect to DataBase in the back end

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#importing dependencies for python
import numpy as np
import os
import datetime as dt
from dateutil.relativedelta import relativedelta
import json
from bson import json_util



#from app import db

######################
# Database Setup
######################

pg_user = 'postgres'
pg_password = 'Dhanista#4'
db_name = 'ETL-Project'

connection_string = f"{pg_user}:{pg_password}@localhost:5433/{db_name}"
engine = create_engine(f'postgresql://{connection_string}')

print(engine)

# reflect an existing database into a new model

Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
#table1 = Base.classes.table1
Income = Base.classes.country_income 
traffiking_details = Base.classes.global_traffiking
Countries = Base.classes.countries

#table3 = Base.classes.table3


######################
# Flask Setup
######################

app = Flask(__name__)
# Create an App

# Define route to homepage

@app.route("/")
def home():
        return (f"Welcome to Our Home Page<br/><br/>"
                f"Available Routes:<br/><br/>"
                f"/api/v1.0/exploit<br/>"
                f"/api/v1.0/income<br/>" 
                f"/api/v1.0/country-codes<br/><br/>"
                f"/api/v1.0/gender-stats<br/><br/>")
                

@app.route("/api/v1.0/gender-stats")
def gender():
    """Gender Stats"""

    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Query the income level and country code from income table
    income = session.query(func.count(traffiking_details.Gender)).group_by(traffiking_details.Gender).all()

    #session.close()
    session.close()

    income_list = list(np.ravel(income))

    
    return jsonify(income_list)


@app.route("/api/v1.0/exploit")
def exploit():
    """List"""

    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Query the income level and country code from income table
    income_q = session.query(Income.countrycode, Countries.country_name, Income.incomelevel).filter(Income.countrycode==Countries.country_code).all()


    #Countries.country_name,Countries.country_code


   #Income.countrycode, Income.incomelevel
    #session.close()
    session.close()

    income_list = []

    for country_income,countries in income_q:
        income_dict = {}
        income_dict["Country_name"] = countries.country_name
        income_dict["Country-Code"] = country_income.countrycode
        income_dict["Income-Level"] = country_income.incomelevel
        income_list.append(income_dict)

    # return JSON list of incomes

    return(jsonify(income_list))



    #pd.read_sql(session.query(EA.sporder, 
     #                     EA.family.label("EA_Family"), 
      #                    EA.genus.label("EA_Genus"), 
       #                   EA.species.label("EA_Species"), 
        #                  NA.family.label("NA_Family"), 
         #                 NA.genus.label("NA_Genus"), 
          #                NA.species.label("NA_Species")).filter(EA.sporder == NA.sporder).limit(10).statement, engine)



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
 
    
    #income_list = list(np.ravel(income))

    
    #return jsonify(income_list)

    income_list = []

    for country_income in income:
        income_dict = {}
        income_dict["Country-Code"] = country_income.countrycode
        income_dict["Income-Level"] = country_income.incomelevel
        income_list.append(income_dict)

    # return JSON list of incomes

    return(jsonify(income_list))

   

    #json_docs = []
    #for doc in income_list:
     #   json_doc = json.dumps(doc, default=json_util.default)
      #  json_docs.append(json_doc)
      

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
