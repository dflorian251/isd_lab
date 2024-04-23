from scholarly import scholarly
import json

# Retrieve the author's data
author = scholarly.search_author_id('HTcDtXsAAAAJ')


result = scholarly.fill(author, sections=["publications"])
print(json.dumps(result["publications"], indent=4))
print(len(result["publications"]))

