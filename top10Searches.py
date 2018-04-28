import sys, webbrowser, requests, bs4

url = 'https://www.google.co.in/search?q=' + '+'.join(sys.argv[1:])

#webbrowser.open(url)

res = requests.get(url)
res.raise_for_status()
print(res.raise_for_status())
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elem = soup.select('.r a')
for element in elem:
    uri = 'https://www.google.co.in/'+element.attrs['href']
    webbrowser.open(uri)
    #print(element.attrs['href'])

#rso > div:nth-child(1) > div > div:nth-child(1) > div > div > h3 > a
#rso > div:nth-child(1) > div > div:nth-child(2) > div > div > h3 > a
#rso > div:nth-child(1) > div > div:nth-child(3) > div > div > h3 > a
#rso > div:nth-child(1) > div > div:nth-child(4) > div > div > h3 > a
#rso > div:nth-child(1) > div > div:nth-child(5) > div > div > h3 > a
#imagebox_bigimages > g-section-with-header > div._ojo > h3 > a
#rso > div:nth-child(3) > div > div:nth-child(1) > div > div > h3 > a
