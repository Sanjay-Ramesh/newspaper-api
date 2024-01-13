import requests
from send_email import send_email

topic = "tesla"

api_key = "50f488bc91474505a8388f4ac83371e9"
url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-12-13&sortBy=publishedAt&apiKey=50f488bc91474505a8388f4ac83371e9&language=en"

#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles and description
body  = ""
for article in content["articles"][:20]:
    body = "Subject: Today's News" + "\n" + body + article["title"] + "\n" + str(article["description"]) +"\n"+article["url"]+ 2*"\n"

body = body.encode("utf-8")
send_email(message=body)