# sqlalchemy-challenge Module 10 Challenge

# Unit 10 Homework: Surf’s Up

![](https://github.com/mugsiemx/sqlalchemy-challenge/blob/main/SurfsUp/Images/sql.jpg)

### Began with

1. Created a new repository for this project called `sqlalchemy-challenge`.
2. Cloned the new repository to local computer.
3. Inside my local Git repository, created a directory for this Challenge. Using a folder name that corresponds to the Challenge, `SurfsUp`.
4. Added my Jupyter notebook and `app.py` to this folder. They’ll contain the main scripts to run for analysis. Also added the `Resources` folder, which contains the data files I will be using for this challenge. Also created an image file to save pictures for README.md file.
5. Pushed the changes to GitHub upon these initial steps.

### Files

Download the following files to help to get started:
[Module 10 Challenge files](https://static.bc-edx.com/data/dl-1-2/m10/lms/starter/Starter_Code.zip)

### Instructions

![](https://github.com/mugsiemx/sqlalchemy-challenge/blob/main/SurfsUp/Images/Hawaii.jpg)

Congratulations to me! My wonderful husband decided to treat us to a long holiday vacation in Honolulu, Hawaii. To help with our trip planning, I decided to do a climate analysis about the area. The following sections outline the steps that I needed to take to accomplish this task.

#### Part 1: Analyze and Explore the Climate Data

In this section, I’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of my climate database. Specifically, I’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, the following steps needed to be completed:

1. I used the provided files (`climate_starter.ipynb` and `hawaii.sqlite`) to complete my climate analysis and data exploration.

2. Used the SQLAlchemy `create_engine()` function to connect to my SQLite database.

3. Use the SQLAlchemy `automap_base()` function to reflect my tables into classes, and then save references to the classes named `station` and `measurement`.

4. Link Python to the database by creating a SQLAlchemy session and closing my session at the end of my notebook.

5. Performed a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

##### Precipitation Analysis

1. Found the most recent date in the dataset.

2. Using that date, got the previous 12 months of precipitation data by querying the previous 12 months of data, without passing the datea as a variable to my query.

3. Selected only the "date" and "prcp" values.

4. Loaded the query results into a Pandas DataFrame, and set the index to the "date" column.

5. Sorted the DataFrame values by "date".

6. Ploted the results by using the DataFrame `plot` method, as the following image shows:

   ![](https://github.com/mugsiemx/sqlalchemy-challenge/blob/main/SurfsUp/Images/PrecipitationsFOR12months.png}

7. Use Pandas to print the summary statistics for the precipitation data.

   ![](https://github.com/mugsiemx/sqlalchemy-challenge/blob/main/SurfsUp/Images/precipitation_summary_statistics.jpg)
   
##### Station Analysis

1. Designed a query to calculate the total number of stations in the dataset.

2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, completed the following steps:

   - Listed the stations and observation counts in descending order by using the func.count funtion in my query.

   - The station id that has the greatest number of observations was station USC00519281, named WAIHEE 837.5, HI US. Used the hint to: Join the station and measurement tables for some of the queries.
   
   ![](https://github.com/mugsiemx/sqlalchemy-challenge/blob/main/SurfsUp/Images/most_active_stations.jpg)

3. Designed a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query by using functions such as `func.min`, `func.max`, and `func.avg` in your query.

   ![](https://github.com/mugsiemx/sqlalchemy-challenge/blob/main/SurfsUp/Images/precipitation_summary_statistics.jpg)

4. Designed a query to get the previous 12 months of temperature observation (TOBS) data. To do so, completed the following steps:

   - Filtered by the station that has the greatest number of observations.

   - Queried the previous 12 months of TOBS data for that station.

   - Ploted the results as a histogram with `bins=12`, as the following image shows:
      
      ![](https://github.com/mugsiemx/sqlalchemy-challenge/blob/main/SurfsUp/Images/PrecipitationsFOR12months.png)
     
5. Closed your session. (Very Important)

#### Part 2: Design Your Climate App

Now that I’ve completed my initial analysis, I’ll design a Flask API based on the queries that I just developed. Used Flask to create my routes as follows:

1. `/`

   - Started at the homepage.
   
   ![](https://github.com/mugsiemx/sqlalchemy-challenge/blob/main/SurfsUp/Images/loccalhost_image.jpg)
   
   - Listed all the available routes.

2. `/api/v1.0/precipitation`

   - Converted the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using `date` as the key and `prcp` as the value.

   - Returned the JSON representation of your dictionary. Used the hint to use the Flask `jsonify` function to convert my API data to a valid JSON response object for each representation going forward.

3. `/api/v1.0/stations`

   - Returned a JSON list of stations from the dataset.

4. `/api/v1.0/tobs`

   - Queried the dates and temperature observations of the most-active station for the previous year of data.

   - Returned a JSON list of temperature observations for the previous year.

5. `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>` (This could have been a looped procedure)

   - Returned a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

   - For a specified start, calculate `TMIN`, `TAVG`, and `TMAX` for all the dates greater than or equal to the start date.

   - For a specified start date and end date, calculate `TMIN`, `TAVG`, and `TMAX` for the dates from the start date to the end date, inclusive.
   
   ![](https://github.com/mugsiemx/sqlalchemy-challenge/blob/main/SurfsUp/Images/last_api_route.jpg)
   
## End of Assignment
   ![](https://github.com/mugsiemx/sqlalchemy-challenge/blob/main/SurfsUp/Images/task_completed.jpg)
photos credit to iStock
