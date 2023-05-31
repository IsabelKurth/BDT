import psycopg2
from textblob import TextBlob

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="customer_data",
    user='postgres',
    password= 'projectwi'
)



# Create a cursor to execute SQL queries
cur = conn.cursor()

# Fetch data from the database
cur.execute("SELECT id, review_text FROM reviews")
rows = cur.fetchall()

# Update the sentiment classification in the database
for row in rows:
    id, text = row

    # Check if the text is not None
    if text is not None:
        # Perform sentiment analysis using TextBlob
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        # Classify the sentiment as negative, neutral, or positive
        if sentiment < 0:
            classification = "negative"
        elif sentiment == 0:
            classification = "neutral"
        else:
            classification = "positive"
    else:
        # If text is None, set sentiment as None
        classification = None
    print(classification)
    # Update the table with the sentiment classification
    cur.execute("UPDATE reviews SET classification=%s WHERE id=%s", (classification, id))

# Commit the changes to the database
conn.commit()

# Close the database connection
cur.close()
conn.close()

