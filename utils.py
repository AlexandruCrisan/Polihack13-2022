# Ignores the articles from youtube
def getNonYouTube(news_dict):
  news_count = 0
  valid_news_articles = []
  for article in news_dict["articles"]:
    if len(valid_news_articles) == 20:
      print("20 news found")
      return valid_news_articles
    if article["source"]["name"] != "YouTube":
      news_count += 1
      valid_news_articles.append(article)
  print(f"{news_count} news found")
  return valid_news_articles

# Removes the source from article title
def removeSourceFromName(articles):
  for article in articles:
    dashIndex = article["title"].rfind('-') # .rfind() is the reverse search (from right to left), searches for the "-" that is always followed by the source name
    article["title"] = article["title"][0:dashIndex - 1]

# Removes the total number of chars displayed at the end of content
def removeCharsNumber(articles):
  for article in articles:
    if article["content"]:
      dashIndex = article["content"].rfind('[')
      article["content"] = article["content"][0:dashIndex]

# Remove the unicode characters from text ("\u203", "\u103" etc)
def removeUnicodeChars(articles):
  for article in articles:
    try:
      encoded = article["content"].encode("ascii", "ignore")
      article["content"] = encoded.decode()
    except AttributeError as a:
      pass

def createJSONFileLocally(jsonObj):
  with open('temp.json', 'w') as file:
    file.write(jsonObj)