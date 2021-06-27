from urllib.request import Request, urlopen
from urllib.parse import quote_plus
import re

#imgrefurl=

def findin(site:str, user:str):
	url = f'https://google.com/search?q={quote_plus(f"site:{site} intext:{user}")}'

	req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})

	response = urlopen(req)

	geturls = re.findall(r'imgrefurl=(https://[\w\.\/\?\=\:\-\_]+)', response.read().decode())


	print(geturls)

findin('twitter.com', 'VoidVoidi')