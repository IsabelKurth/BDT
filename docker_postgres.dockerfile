# run postgres image
docker pull postgres

# start postgres containter BDT
docker run --name BDT -e POSTGRES_PASSWORD=projectwi -d -p postgres
docker exec -it BDT psql -U postgres
\l
CREATE DATABASE customers_text;
\c customers_text
CREATE TABLE reviews (
  id INTEGER,
  clothing_id INTEGER,
  age INTEGER,
  title TEXT,
  review_text TEXT,
  rating INTEGER,
  recommended_ind INTEGER,
  positive_feedback_count INTEGER,
  division_name TEXT,
  department_name TEXT,
  class_name TEXT
);
\d reviews 
\q


docker cp clothing.csv BDT:/clothing.csv
docker exec -it BDT psql -U postgres
\c customers_text

COPY reviews(id, clothing_id, age, title, review_text, rating, recommended_ind, positive_feedback_count, division_name, department_name, class_name)
FROM '/clothing.csv'
DELIMITER ','
CSV HEADER;

\d reviews
SELECT COUNT(*) FROM reviews; 

