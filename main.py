from scholarly import scholarly
from serpapi import GoogleSearch
import json
from dotenv import load_dotenv
import yaml
import os
import requests



def get_member_scholar(parameters, start):
	parameters["start"] = start
	search = GoogleSearch(parameters)
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
	
	load_dotenv()
	API_KEY = os.getenv("SARPAPI_API_KEY")


	for author_id in authors_ids:
		if (author_id == None):
			continue

		# Write the publications
		author = scholarly.search_author_id(author_id)
		author_interests = author["interests"]
		result = scholarly.fill(author, sections=["publications"])
		author_name = get_member_name(author_id)
		author = [
				{"author_name": author_name},
				{"interest": author_interests}
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

		params = {
			"api_key": API_KEY,
			"engine": "google_scholar_author",
			"hl": "en",
			"author_id": author_id,
		}

		# Write the publications in citation friendly format
		# This code was added because the page needs to display the publications of each author in APA format
		result = get_member_scholar(params, start_param)
		data = result["articles"]
		count = 0
		while count <= start_param:
			next_url = result["serpapi_pagination"]["next"]
			result = requests.get(next_url, params).json()
			data = data + result["articles"]
			count += 1
		
		data = [author, data]
		data = json.dumps(data, indent=4)
		data = f"{data},N/N" # N/N indicates that there should be start a newline. Couldn't in a different way start a newline :/
		data = data.replace("N/N", '\n')
		# with open("./_data/citations.json", "a+") as file:
		# 	file.write(data)
		# 	file.close()
		
	

	print("Loop finished")


	# # EDIT THE PUBLICATIONS FILE
	print("Getting ready to edit the file")
	with open(f"./assets/publications.json", "a+") as file:
		print('File opened for reading')
		file.seek(0) # Because in a+ mode the cursor is by default at the end of the file
		contents = file.read()
		file.close()

	contents = f"[{contents}]"
	contents = contents[:len(contents)-3] + contents[len(contents)-3+1:] # Remove the last comma for syntax reasons
	json_contents = json.dumps(json.loads(contents), indent=4)
	# Use of w+ mode because we don't want the previous file's content
	with open(f"./assets/publications.json", "w+") as file:
		print("File opened for writing")
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
	print(json_contents)
	# Use of w+ mode because we don't want the previous file's content
	with open(f"./_data/citations.json", "w+") as file:
		file.write(json_contents)
		file.close()
	
