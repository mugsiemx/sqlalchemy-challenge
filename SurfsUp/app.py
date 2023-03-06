# Climate App

# Set up and Import Dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt
from datetime import timedelta, date

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################
# all available api routes


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to Sheila's Climate app!!<br/>"
        f"<br>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/temperature<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

# 1 of 5 api routes

# 1 of 5 api routes
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Convert the query results from your precipitation analysis to a dictionary using `date` as the key and `prcp` as the value
    # (i.e. retrieve only the last 12 months of data)
    # Query precipitation

    # get the last recorded date in the table and calculate the one year ago starting point date
    # set up variables
    recent_date_str = session.query(func.max(Measurement.date)).one()[0]
    for recent_date in recent_date_str:
        recent_date = dt.datetime.strptime(recent_date_str, "%Y-%m-%d")

    one_year_ago = recent_date - timedelta(days=365)
    # query the results as above
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).\
        order_by(Measurement.date).all()
    # close this session
    session.close()
  # Create a dictionary from the row data and append to a list of all_precipitations
    all_precipitations = []
    for date, prcp in results:
        precipitations_dict = {}
        precipitations_dict["date"] = date
        precipitations_dict["prcp"] = prcp
        all_precipitations.append(precipitations_dict)
    return jsonify(all_precipitations)

# 2 of 5 api routes
@ app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of weather stations"""
    # Query all stations
    results = session.query(Station.station, Station.name,
                            Station.latitude, Station.longitude, Station.elevation).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_stations
    all_stations = []
    for station, name, latitude, longitude, elevation in results:
        stations_dict = {}
        stations_dict["station"] = station
        stations_dict["name"] = name
        stations_dict["latitude"] = latitude
        stations_dict["longitude"] = longitude
        stations_dict["elevation"] = elevation
        all_stations.append(stations_dict)

    return jsonify(all_stations)

# 3 of 5 api routes
@ app.route("/api/v1.0/temperature")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of temperatures"""
    # first locate the most active weather station
    most_active_station_result = session.query(Measurement.station).\
        group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()        
    most_active_station = most_active_station_result[0]
    # next locate the most recent date observed and the date a year ago from that date
    # date recent
    recent_date_str = session.query(func.max(Measurement.date)).one()[0]
    for recent_date in recent_date_str:
        recent_date = dt.datetime.strptime(recent_date_str, "%Y-%m-%d")

    one_year_ago = recent_date - timedelta(days=365)
    # query the results as above
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= one_year_ago).\
        order_by(Measurement.date).all()
    # close this session
    session.close()
  # Create a dictionary from the row data and append to a list of all_precipitations
    all_temperatures = []
    for date, tobs in results:
        temperatures_dict = {}
        temperatures_dict["date"] = date
        temperatures_dict["tobs"] = tobs
        all_temperatures.append(temperatures_dict)

    return jsonify(all_temperatures)

# 4 of 5 api routes
@ app.route("/api/v1.0/<start>")
def start(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # string date in api route convert to date format
    start_date = dt.datetime.strptime(start, '%Y-%m-%d')

    """Return a list of temperature min, max, avg for a start_date through the last observed"""
    # query the results as above
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    # close this session
    session.close()
  # Create a dictionary from the row data and append to a list of all_precipitations
    all_functions = []
    for min, max, avg in results:
        functions_dict = {}
        functions_dict["Minimum_Temperature"] = min
        functions_dict["Maximum_Temperature"] = max
        functions_dict["Average_Temperature"] = avg
        all_functions.append(functions_dict)

    return jsonify(all_functions)

# 5 of 5 api routes
@ app.route("/api/v1.0/<start>/<end>")
def both(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # string date in api route convert to date format
    start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    end_date = dt.datetime.strptime(end, '%Y-%m-%d')

    """Return a list of temperature min, max, avg for a start_date through the last observed"""
    # query the results as above
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start_date).\
        filter(Measurement.date <= end_date).all()
    # close this session
    session.close()
  # Create a dictionary from the row data and append to a list of all_precipitations
    all_functions = []
    for min, max, avg in results:
        functions_dict = {}
        functions_dict["Minimum_Temperature"] = min
        functions_dict["Maximum_Temperature"] = max
        functions_dict["Average_Temperature"] = avg
        all_functions.append(functions_dict)

    return jsonify(all_functions)
#################################################
# Flask App to run in terminal with python app.py
#################################################
if __name__ == '__main__':
    app.run(debug=True)
