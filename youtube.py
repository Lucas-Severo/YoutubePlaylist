import requests
import json
import math

token = "yourToken"

url = "Playlist Link"
index = url.find("list=")

playlistId = url[index+5:]
maxResults = 50 # máximo de 50 vídeos por página

url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet%2CcontentDetails&maxResults={maxResults}&playlistId={playlistId}&key={token}"

try:
	r = requests.get(url).json()
	page = 1
	cont = 1
	response = r['items']
	## verifica quantas páginas existem
	pages = math.ceil(r['pageInfo']['totalResults']/r['pageInfo']['resultsPerPage'])
		
	print(f"playlistLink: https://www.youtube.com/playlist?list={response[0]['snippet']['playlistId']}\n")

	if pages >= 1:
		## pega 50 vídeos para cada página que existir na playlist
		while page <= pages:
			try:
				nextPage = r['nextPageToken']
				url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&pageToken={nextPage}&playlistId={playlistId}&key={token}"
			except:
				print()

			for item in response:
				title = item['snippet']['title']
				if title != "Private video":
					print(f"Video {cont}")
					print(f"Title: {item['snippet']['title']}")
					print(f"publishedAt: {item['snippet']['publishedAt']}")
					print(f"Link: https://www.youtube.com/watch?v={item['snippet']['resourceId']['videoId']}")
					print(f"Thumbnail: {item['snippet']['thumbnails']['high']['url']}\n")
				cont += 1

			r = requests.get(url).json()
			response = r['items']
			page += 1
except Exception as e:
	print("Connection Error")

