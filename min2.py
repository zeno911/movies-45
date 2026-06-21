from bs4 import BeautifulSoup

import requests


yc_url = "https://news.ycombinator.com/"

response = requests.get(yc_url)
yc_page = response.text
soup = BeautifulSoup(yc_page, "html.parser")

articles = soup.find_all(name= "span", class_="titleline")
article_texts = []
article_links = []
for article in articles:
    
    a = article.find("a")
    
    text = a.get_text()
    article_texts.append(text)
    article_links.append(a['href'])
    
    
    


score = [int(score.getText().split()[0]) for score in soup.find_all(name= "span", class_ = "score")]



score_index = score.index(max(score))

print(score_index)
print(article_texts[score_index],article_links[score_index])