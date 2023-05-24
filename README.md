# BDT

# Docker and PostgreSQL Setup

Pull the PostgreSQL image from Docker Hub:
```console
docker pull postgres
```

Create a new container with the name "bdt_custexp" and the PostgreSQL image:
```console
docker create --name bdt_custexp -e POSTGRES_PASSWORD=bdt_isawiebz postgres
```

Start the container:
```console
docker start bdt_custexp
```

Connect to the PostgreSQL container:
```console
docker exec -it bdt_custexp psql -U postgres
```

Interact with the PostgreSQL database:
```console
CREATE DATABASE cust_reviews;
```

Connect to a specific database:
```console
\c cust_reviews;
```

Create a new table:
```console
CREATE TABLE mytable (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  age INTEGER
);
```

Transfer the dataset file to the Docker container:
```console
docker cp e-comm_rev.csv bdt_custexp:/e-comm_rev.csv
```

Connect to the PostgreSQL container:
```console
docker exec -it bdt_custexp psql -U postgres
```

Create a table in the database:
```console
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
```

Import the CSV data into the table:
```console
COPY reviews(id, clothing_id, age, title, review_text, rating, recommended_ind, positive_feedback_count, division_name, department_name, class_name)
FROM '/e-comm_rev.csv'
DELIMITER ','
CSV HEADER;
```


Exit the PostgreSQL container:
```console
\q
```






