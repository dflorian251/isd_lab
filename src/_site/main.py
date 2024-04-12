import argparse
from serpapi import GoogleSearch
import json


def search_publications(author_id):
	params = {
	  "api_key": "3fb752895c99e19a0ed6b6fb1f90f27897cc533c2a2ff520d2a0b5a4bc33ce60",
	  "engine": "google_scholar_author",
	  "hl": "en",
	  "author_id": author_id
	}
	search = GoogleSearch(params)
	results = search.get_dict()
	return results


def output_file(author_name, articles):
	x = articles["articles"]
	y = json.dumps(x, indent=4)
	with open(f"./_data/publications/{author_name}.json", "w") as outfile:
	    outfile.write(y)
	    
	    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get the author's publications")
    parser.add_argument("author_id", type=str, help="Parameter defines the ID of an author. You can find the ID by going to the Google Scholar author's profile page and getting it from there (e.g., https://scholar.google.com/citations?user={author_id}).")
    parser.add_argument("author_name", type=str, help="The field url in the staff.yml file.")
    args = parser.parse_args()
    
    articles = search_publications(args.author_id)
    output_file(args.author_name, articles)
    
    

