import sys, termios, tty, glob, os

def init(**kw):
  make_find_all_files(**kw)

class Pinata:
  def __getattr__(self, key):
    print 'getting:', key
    return
pinata = Pinata()

def make_find_all_files(dir_path):
  path_to_text = {}

  for path in glob.glob(os.path.join(dir_path, '*')):
    with open(path) as f:
      text = f.read()
    path_to_text[path] = text.lower()

  def find_all_files():
    matches = []
    query_lower = query_string.lower()

    for path in glob.glob(os.path.join(dir_path, '*')):
      if query_lower in path:
        matches.append(path)

      if query_string in path_to_text:
        matches.append(path)
    return matches
  return find_all_files

find_all_files = make_find_all_files()

def is_letter(ch):
  return ch.isalpha()

def wait_for_key():
  # Return a single character from stdin.

  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
  return ch
