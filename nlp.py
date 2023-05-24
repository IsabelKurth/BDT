import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd
import numpy as np

# Load spaCy model and add the SpacyTextBlob component
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")

# Function to classify sentiment
def classify_sentiment(text):

    if isinstance(text, float) and np.isnan(text):
        return "neutral"

    doc = nlp(text)
    polarity = doc._.polarity

    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"


# Sample DataFrame with text column
df = pd.read_csv('clothing.csv')
"""
data = {
    "text": [
        "I love this product!",
        "It was a terrible experience.",
        "The weather is nice today.",
        "I'm feeling neutral about it."
    ]
}
df = pd.DataFrame(data)
"""

# Apply sentiment classification to the text column
df["sentiment"] = df["Review Text"].apply(classify_sentiment)

# Display the updated DataFrame
print(df)


"""
#with spark 
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Create SparkSession
spark = SparkSession.builder.getOrCreate()

# Load spaCy model and add the SpacyTextBlob component
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")

# Register UDF for sentiment classification
classify_sentiment_udf = udf(lambda text: classify_sentiment(text), StringType())

# Sample DataFrame with text column
data = [("I love this product!",),
        ("It was a terrible experience.",),
        ("The weather is nice today.",),
        (None,)]  # Example with null value
df = spark.createDataFrame(data, ["text"])

# Apply sentiment classification using UDF
df = df.withColumn("sentiment", classify_sentiment_udf("text"))

# Display the updated DataFrame
df.show()

"""
