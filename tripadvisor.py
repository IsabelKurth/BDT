import requests
from bs4 import BeautifulSoup

# URL of the TripAdvisor page with customer reviews
url = "https://www.tripadvisor.com/Hotel_Review-g187147-d197468-Reviews-Hotel_Eiffel_Turenne-Paris_Ile_de_France.html"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find all review containers on the page
review_containers = soup.find_all("div", class_="review-container")

# Iterate over each review container
for review in review_containers:
    # Extract review text
    review_text = review.find("div", class_="entry").find("p").text.strip()

    # Extract rating
    rating = review.find("span", class_="ui_bubble_rating")["class"][1].split("_")[-1]

    # Extract review date
    review_date = review.find("span", class_="ratingDate")["title"]

    # Print the extracted information
    print("Review Text:", review_text)
    print("Rating:", rating)
    print("Review Date:", review_date)
    print("------------------------")