import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = 'https://www.wakfu.com/fr/mmorpg/encyclopedie/armures'

ua = UserAgent()
headers = {'User-Agent': ua.chrome}
session = requests.Session()
response = requests.get(url, headers=headers)
cookies = response.cookies
response = session.get(url, cookies=cookies)

#response = requests.get(url)
soup = BeautifulSoup("./html_wakfu.html", 'html.parser')



table = soup.find('table', {'class': 'ak-table ak-responsivetable'})



rows = table.find_all('tr')

data = []
for row in rows[1:]:
    cols = row.find_all('td')
    cols = [col.text for col in cols]
    data.append(cols)

print(data)