# BDT: Project Customer Sentiment Analysis

## 0. Step: Preprocessing of csv file
clothing.csv file from Kaggle has unquoted new lines. This makes trouble when uploading it to postgres database. Therefore run preprocessing.py to use quoted csv field. Output file is clothing_updates.csv. 

## 1. Step: Docker and Postgres Database
Run commands in the docker_postgres.txt file in a command prompt to create the database and load the dataset from kaggel into it (clothing_updates.csv). 

## 2.Step: NLP 
Use Spacey to do the sentiment analysis of the review texts. Run docker_NLP.py and adapt eventually connection to the database according to your configurations. 
Updated file with classification of the review text is saved in column classification in reviews table in database. 
(Downloaded in reviews.csv) 

## 3.Step: Visualization in Tableau 
Connect with Tableau desctop to Postgres database customers_data. 


