'''
find all files that match the query
'''

class Searcher:
  def __init__(self, dir_path):
    self.basename_to_content = {}
    self.basename_to_content_lower = {}
    glob_path = os.path.join(dir_path, '*.txt')
    for path in glob.glob(glob_path):
      basename = os.path.splitext(os.path.basename(path))[0]
      with open(path) as f:
        self.basename_to_content[basename] = f.read()
      self.basename_to_content_lower[basename] = self.basename_to_content[basename].lower()

  def search(basename_to_content_lower, query_string, score):
    matched_basenames = []

    terms = set(query_string.lower().split())
    for basename in basename_to_content_lower.keys():
      content = basename_to_content_lower[basename]
      for term in terms:
        if term not in basename and term not in content:
          break
      else:
        matched_basenames.append(basename)

    matched_basenames.sort(key=score, reverse=True)
    return matched_basenames
