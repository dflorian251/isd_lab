import argparse
from serpapi import GoogleSearch
import json
from dotenv import load_dotenv
import os
import yaml

def get_authors_ids():
	with open('_data/staff.yml', 	'r') as f:
		staff_data = yaml.full_load(f)
	authors_ids = []
	for i in range (0, len(staff_data)):
		authors_ids.append(staff_data[i]["author_id"])
	return authors_ids


def get_author_url(author_id):
	with open('_data/staff.yml', 'r') as f:
		staff_data = yaml.full_load(f)
	for i in range (0, len(staff_data)):
		if ( staff_data[i]["author_id"] == author_id):
			return staff_data[i]["url"]
		

def search_publications(author_id, api_key):
	params = {
	  "api_key": api_key,
	  "engine": "google_scholar_author",
	  "hl": "en",
	  "author_id": author_id
	}
	search = GoogleSearch(params)
	results = search.get_dict()
	return results


def output_file(author_url, articles):
	x = articles["articles"]
	y = json.dumps(x, indent=4)
	with open(f"./_data/publications/{author_url}.json", "w") as outfile:
	    outfile.write(y)
	    
	    
if __name__ == "__main__":

	load_dotenv()
	api_key = os.getenv("SARPAPI_API_KEY")
	authors_list = get_authors_ids()
	for author_id in authors_list:
		author_url = get_author_url(author_id)
		articles = search_publications(author_id, api_key)
		output_file(author_url, articles)	
	

    

