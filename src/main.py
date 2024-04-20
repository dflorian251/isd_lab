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


def get_members_names():
	with open('_data/staff.yml', 	'r') as f:
		staff_data = yaml.full_load(f)
	authors_names = []
	for i in range (0, len(staff_data)):
		authors_names.append(staff_data[i]["name"])
	return authors_names


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


 
	    
	    
if __name__ == "__main__":

	load_dotenv()
	api_key = os.getenv("SARPAPI_API_KEY")
	members_list = get_members_ids()
	for author_id in members_list:
		if (author_id == None):
			continue
		member_data = get_member_scholar(author_id, api_key)
		author = [
				{"author_id": author_id}
		]
		data = [author, member_data["articles"]]
		data = json.dumps(data, indent=4)
		data = f"{data},N/N" # N/N indicates that there should be start a newline. Couldn't in a different way start a newline :/
		data = data.replace("N/N", '\n')
		with open(f"./_data/publication.json", "a+") as file:
			file.write(data)
			file.close(data)

	with open(f"./_data/publication.json", "a+") as file:
		file.seek(0) # Because in a+ mode the cursor is by default at the end of the file
		contents = file.read()
		file.close()
	
	contents = f"[{contents}]"
	contents = contents[:len(contents)-3] + contents[len(contents)-3+1:] # Remove the last comma for syntax reasons
	json_contents = json.dumps(json.loads(contents), indent=4)
	# Use of w+ mode because we don't want the previous file's content
	with open(f"./_data/publication.json", "w+") as file:
		file.write(json_contents)
		file.close()
	
	