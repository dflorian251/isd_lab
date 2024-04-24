from scholarly import scholarly
from serpapi import GoogleSearch
import json
from dotenv import load_dotenv
import yaml
import os



def get_member_scholar(author_id, api_key, start_param):
	params = {
	  "api_key": api_key,
	  "engine": "google_scholar_author",
	  "hl": "en",
	  "author_id": author_id,
	  "start": start_param
	}
	search = GoogleSearch(params)
	results = search.get_dict()
	return results


def get_members_ids():
	with open('_data/staff.yml', 	'r') as f:
		staff_data = yaml.full_load(f)
	authors_ids = []
	for i in range (0, len(staff_data)):
		authors_ids.append(staff_data[i]["author_id"])
	return authors_ids


def get_member_name(search_id):
	with open('_data/staff.yml', 	'r') as f:
		staff_data = yaml.full_load(f)
	for i in range (0, len(staff_data)):
		if staff_data[i]["author_id"] == search_id:
			return staff_data[i]["name"]




	    
if __name__ == "__main__":
	authors_ids = get_members_ids()
	for author_id in authors_ids:
		if (author_id == None):
			continue

		# Write the publications
		author = scholarly.search_author_id(author_id)
		result = scholarly.fill(author, sections=["publications"])
		author_name = get_member_name(author_id)
		author = [
				{"author_name": author_name}
		]
		data = [author, result["publications"]]
		data = json.dumps(data, indent=4)
		data = f"{data},N/N" # N/N indicates that there should be start a newline. Couldn't in a different way start a newline :/
		data = data.replace("N/N", '\n')
		with open(f"./assets/publications.json", "a+") as file:
			file.write(data)
			file.close()


		# Calculate how many pages need to be fetched
		num_publications = len(result["publications"])
		if num_publications <= 20:
			start_param = 0
		else :
			start_param = num_publications // 100
			if num_publications % 100 != 0 :
				start_param += 1

		# Write the publications in citation friendly format
		# This code was added because the page needs to display the publications of each author in APA format
		load_dotenv()
		api_key = os.getenv("SARPAPI_API_KEY")
		result = get_member_scholar(author_id, api_key, start_param)
		citations = json.dumps(result["articles"], indent=4)
		citations = f"{citations},N/N" # N/N indicates that there should be start a newline. Couldn't in a different way start a newline :/
		citations = citations.replace("N/N", '\n')
		with open("./_data/citations.json", "a+") as file:
			file.write(citations)
			file.close()




	# EDIT THE PUBLICATIONS FILE
	with open(f"./assets/publications.json", "a+") as file:
		file.seek(0) # Because in a+ mode the cursor is by default at the end of the file
		contents = file.read()
		file.close()
	
	contents = f"[{contents}]"
	contents = contents[:len(contents)-3] + contents[len(contents)-3+1:] # Remove the last comma for syntax reasons
	json_contents = json.dumps(json.loads(contents), indent=4)
	# Use of w+ mode because we don't want the previous file's content
	with open(f"./assets/publications.json", "w+") as file:
		file.write(json_contents)
		file.close()

	# EDIT THE CITATIONS FILE
	with open(f"./_data/citations.json", "a+") as file:
		file.seek(0) # Because in a+ mode the cursor is by default at the end of the file
		contents = file.read()
		file.close()
	
	contents = f"[{contents}]"
	contents = contents[:len(contents)-3] + contents[len(contents)-3+1:] # Remove the last comma for syntax reasons
	json_contents = json.dumps(json.loads(contents), indent=4)
	# Use of w+ mode because we don't want the previous file's content
	with open(f"./_data/citations.json", "w+") as file:
		file.write(json_contents)
		file.close()
	
