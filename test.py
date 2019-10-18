import math
import sys
import urllib.request
import yaml

from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials

n_images_per_request = 150

def download_images(yaml_file = "ship.yaml", subscription_key = "c92f38127c76493b93a2a739b21fae32")
	
	with open(yaml_file, 'r') as stream: task_params = yaml.safe_load(stream)
	n_requests = math.ceil(task_params['no_of_images']/150)

	i=0
	client = ImageSearchAPI(CognitiveServicesCredentials(subscription_key))

	for page_no in range(n_requests):
		
		image_results = client.images.search(**task_params['query_params'])

		for img in image_results.value:
			print(f'Downloading {img.content_url}')
			try:
				urllib.request.urlretrieve(img.content_url, f'img/{i}.jpg')    	
				i += 1
			except:
				print("Unexpected error:", sys.exc_info()[0])
			if i >= task_params['no_of_images']: return

