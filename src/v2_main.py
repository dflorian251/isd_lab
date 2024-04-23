from scholarly import scholarly
import json
import yaml



def get_members_ids():
	with open('_data/staff.yml', 	'r') as f:
		staff_data = yaml.full_load(f)
	authors_ids = []
	for i in range (0, len(staff_data)):
		authors_ids.append(staff_data[i]["author_id"])
	return authors_ids


	    
if __name__ == "__main__":
	authors_ids = get_members_ids()
	for author_id in authors_ids:
            author = scholarly.search_author_id(author_id)

            result = scholarly.fill(author, sections=["publications"])
            print(json.dumps(result["publications"], indent=4))
            print(len(result["publications"]))

