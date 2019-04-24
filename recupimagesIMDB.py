
#-=-=-=-=-=-=-=-=-=-=-#
#       IMPORT        #
#-=-=-=-=-=-=-=-=-=-=-#

import urllib.request
import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm

#-=-=-=-=-=-=-=-=-=-=-#
#     GET DATA        #
#-=-=-=-=-=-=-=-=-=-=-#

with open('movie_metadata.csv', newline='') as csvfile:

	for i in range(2392):
		csvfile.readline()
	films = csv.reader(csvfile)

	for row in tqdm(films):
		titre = row[11]
		titre = titre.replace("/","")
		genres = row[9]
		url = row[17]
		nom_poster = titre + "__" + genres + ".jpg"

		try:
			page = urllib.request.urlopen(url)
			soup = BeautifulSoup(page, "html.parser")
			poster_div = soup.find("div", attrs={"class": "poster"})
			image_url =poster_div.img['src']
			img_data = requests.get(image_url).content
			with open("posters/" + nom_poster, 'wb') as handler:
				handler.write(img_data)
		except:
			pass
