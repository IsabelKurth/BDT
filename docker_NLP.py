import psycopg2
from textblob import TextBlob

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port="2375",
    database="bdt_custexp",
    user="isabelkurth",
    password="kRM+(.p8$MmhrE!"
)

# Create a cursor to interact with the database
cur = conn.cursor()

# Query the database to fetch the text column from your table
cur.execute("SELECT review_text FROM reviews")
rows = cur.fetchall()

# Iterate over the rows and classify the text using TextBlob
for row in rows:
    text = row[0]  # Assuming the text column is the first column in the table
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Classify the text based on the polarity value
    if polarity > 0:
        classification = "Positive"
    elif polarity < 0:
        classification = "Negative"
    else:
        classification = "Neutral"

    # Update the database with the classification result
    cur.execute("UPDATE reviews SET classification = %s WHERE text_column = %s", (classification, text))
    conn.commit()

# Close the cursor and the database connection
cur.close()
conn.close()
