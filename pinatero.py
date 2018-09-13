import re, sys

with open(sys.argv[1]) as f:
  text = f.read()

queries = re.findall(r'\bpinata\.(.+?)\(', text)
print queries

query_to_pinata_func = {}
for query in queries:
  query_to_pinata_func[query] = database.find(query)
