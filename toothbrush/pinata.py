import sys, termios, tty, glob, os

def is_letter(ch):
  return ch.isalpha()

class FindAllFiles:
  path_to_text = {}

def init_find_all_files(dir_path):
  FindAllFiles.dir_path = dir_path
  for path in glob.glob(os.path.join(dir_path, '*')):
    with open(path) as f:
      text = f.read()
    FindAllFiles.path_to_text[path] = text.lower()

def find_all_files(query_string):
  matches = []
  query_lower = query_string.lower()

  for path in glob.glob(os.path.join(FindAllFiles.dir_path, '*')):
    if query_lower in path:
      matches.append(path)

    if query_string in FindAllFiles.path_to_text[path]:
      matches.append(path)
  return matches

class Pinata:
  pass
pinata = Pinata()
pinata.is_letter = is_letter
pinata.init_find_all_files = init_find_all_files
pinata.find_all_files = find_all_files
