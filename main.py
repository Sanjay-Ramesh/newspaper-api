import requests

api_key = "50f488bc91474505a8388f4ac83371e9"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-12-13&sortBy=publishedAt&apiKey=50f488bc91474505a8388f4ac83371e9"

#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])