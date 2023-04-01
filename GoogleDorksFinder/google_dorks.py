import requests
from bs4 import BeautifulSoup
import datetime


FILE_CREATION_DATE = datetime.datetime.now()

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
}



DORK = input('Input your dork here:\n')
DORK_OUTPUT_FILE = open(f"DORK_{FILE_CREATION_DATE.strftime('%d-%m-%y_%I-%M-%S-%p')}.txt", "a+")
DORK = DORK.replace(' ', '%20')


url = 'https://www.google.com/search?q='+DORK+'&rlz=1C1CHBF_frFR901FR901&oq='+DORK


req = requests.get(url, headers = headers)
soup = BeautifulSoup(req.text, "html.parser")

divs = soup.find('div', id='rso')

a_tags = divs.find_all('div', class_='yuRUbf')

for div in a_tags:
	FIND_LINK = div.find('a', href = True)
	print(FIND_LINK.attrs['href'])
	DORK_OUTPUT_FILE.write(FIND_LINK.attrs['href'] + '\n')

