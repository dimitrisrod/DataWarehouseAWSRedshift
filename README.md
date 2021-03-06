# Project: Sparkify Data Warehouse for Song Play Analysis

A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Main Project Steps

- Extracting data from S3 bucket
- Loading data into Redshift Staging tables.
- Transforming data into a star schema / dimensional tables for analytics consumption.
- Running queries and analysing.

## Datasets

Song data: s3://udacity-dend/song_data
Log data: s3://udacity-dend/log_data
Log data json path: s3://udacity-dend/log_json_path.json

## Database Design

Star Schema is used for the design of this database.

The "songplays" table is the fact table with auto incrementing id and references to 4 dimension tables:
- users
- songs
- artists
- times