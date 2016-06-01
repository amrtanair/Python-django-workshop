#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page
query = raw_input('Search ?')
print query
res = requests.get('http://google.com/search?q=' + 'query')
res.text
# this prints the html file in the terminal.
#what we just did is done using the request module. we are basically copying down
#the web page in html to res
#

# TODO: Retrieve top search result links.

#Next, to scrape through the file using the beautifulsoup libraru and pick out the search results.

import requests, sys, webbrowser, bs4


# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
linkElems = soup.select('.r a')

#Now, we just print it out
for items in linkElems:
    print items.get('href')[7:]
