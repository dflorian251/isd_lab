import argparse
from serpapi import GoogleSearch
import json
from dotenv import load_dotenv
import os
import yaml

def get_members_ids():
	with open('_data/staff.yml', 	'r') as f:
		staff_data = yaml.full_load(f)
	authors_ids = []
	for i in range (0, len(staff_data)):
		authors_ids.append(staff_data[i]["author_id"])
	return authors_ids


# def get_author_url(author_id):
# 	with open('_data/staff.yml', 'r') as f:
# 		staff_data = yaml.full_load(f)
# 	for i in range (0, len(staff_data)):
# 		if ( staff_data[i]["author_id"] == author_id):
# 			return staff_data[i]["url"]
		

def get_member_scholar(author_id, api_key):
	params = {
	  "api_key": api_key,
	  "engine": "google_scholar_author",
	  "hl": "en",
	  "author_id": author_id
	}
	search = GoogleSearch(params)
	results = search.get_dict()
	return results


def output_file(y):
	with open(f"./_data/publications.json", "w+") as outfile:
	    outfile.write(y)
 
	    
	    
if __name__ == "__main__":

	load_dotenv()
	api_key = os.getenv("SARPAPI_API_KEY")
	members_list = get_members_ids()
	print(members_list)
	for author_id in members_list:
		if (author_id == None):
			continue
		member_data = get_member_scholar(author_id, api_key)
		author_info = json.dumps(member_data["author"], indent=4)
		author_articles = json.dumps(member_data["articles"], indent=4)
		author_data = author_info + author_articles
		output_file(author_data)	
		#print(author_data)
	

    

