import sys
import urllib.request

from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials

subscription_key = "c92f38127c76493b93a2a739b21fae32"
search_term = "cruise ship"
client = ImageSearchAPI(CognitiveServicesCredentials(subscription_key))
n_requests = 5
n_images_per_request = 150


i=0

for page_no in range(n_requests):
	
	image_results = client.images.search(query=search_term, count=n_images_per_request, offset=page_no*n_images_per_request)

	for img in image_results.value:
		print(f'Downloading {img.content_url}')
		try:
			urllib.request.urlretrieve(img.content_url, f'img/{i}.jpg')    	
			i += 1
		except:
			print("Unexpected error:", sys.exc_info()[0])

