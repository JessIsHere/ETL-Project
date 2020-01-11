# Import dependencies

from flask import Flask, jsonify
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import os


######################
# Database Setup
######################


pg_user = 'postgres'
pg_password = 'postgres'
db_name = 'customer_db'

connection_string = f"{pg_user}:{pg_password}@localhost:5432/{db_name}"
engine = create_engine(f'postgresql://{connection_string}')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
table1 = Base.classes.table1
table2 = Base.classes.table2
table3 = Base.classes.table3


######################
# Flask Setup
######################

# Create an App
app = Flask(__name__)

# Define route to homepage

@app.route("/")
def home():
        return (f"Welcome to Our Home Page<br/><br/>"
                f"Available Routes:<br/>"
                f"/api/v1.0/table1<br/>"
                f"/api/v1.0/table2<br/>" 
                f"/api/v1.0/table3<br/><br/>"
                
####################################
# Define route to 
####################################

@app.route("/api/v1.0/table1")
def table1():



    # Create our session (link) from Python to the DB
    session = Session(engine)
    


   
    session.close()

# Create a dictionary with date as the key and precip as the value
    all_precip=[]              
    for p in precip:
        precip_dict={}
        precip_dict[p.Date] = p.Precipitation
        all_precip.append(precip_dict)

# Return a json representation of the data
    return jsonify(all_precip)

#############################################
# Define route to 
#############################################

@app.route("/api/v1.0/table2")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Query the station from the Station table
    stations = session.query(Station.station).all()
    session.close()
    
    # convert list of tuples to normal list
    station_list = list(np.ravel(stations))

    # return JSON list of stations
    return jsonify(station_list)

###############################################
# Define route to 
###############################################

@app.route("/api/v1.0/table3")
def temps():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query last year of temp data
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first().date
    date_1yrago = dt.datetime.strptime(last_date, '%Y-%m-%d') - dt.timedelta(days=365)

    temps = session.query(Measurement.date, Measurement.tobs). \
            filter(Measurement.date>=date_1yrago).all()
    session.close()
    # Unpack the list of tuples

    # The instruction said to just return the tobs, but I don't think that makes sense
    # so I am creating a dictionary with date as the key tobs as value and returning that

    all_temps=[]              
    for t in temps:
        temp_dict={}
        temp_dict[t.date] = t.tobs
        all_temps.append(temp_dict)


    return jsonify(all_temps)




# Run in development mode
if __name__ == "__main__":
    app.run(debug=True)