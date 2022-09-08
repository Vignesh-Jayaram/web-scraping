# importing dependencies
from bs4 import BeautifulSoup
import requests
import pprint 

# request and get the context of the url
res = requests.get("https://news.ycombinator.com/")

# check response code and readtext
print(res.status_code)
print(res.text)

# input the text into BeautifulSoup and parse it
soup = BeautifulSoup(res.text, "html.parser")

# Check the properties of the parsed data
print(soup.text)
title = soup.find_all('title')
print(title) 
a_tags = soup.find_all('a')
print(a_tags) # returns the list of 'a' tags in the file


# Collect the data needed in a variable
    # links and subtexts
links = soup.select('.titlelink')
subtexts = soup.select(".subtext")


#create a custom function to filter the data
def custom_hn(links, subtexts):
    hn = []
    for idx, link in enumerate(links):
        title = link.getText()
        href = link.get('href', None)
        vote = subtexts[idx].select('.score')
        if len(vote):
            score = int(vote[0].getText().replace(' points', ''))
            if score > 99:
                hn.append({'heading':title, 'link': href, 'points':score})
   
    return sort_by_points(hn)


def sort_by_points(hn_list):
    return sorted(hn_list, key=lambda k:k['points'], reverse=True)
        
pprint.pprint(custom_hn(links, subtexts))