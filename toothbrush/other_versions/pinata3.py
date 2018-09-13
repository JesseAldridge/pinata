import sys, termios, tty, glob, os

def init(kw):
  candies = [FindAllFiles(kw), WaitForKey(), IsLetter()]

class Pinata:
  def __getattr__(self, key):
    print 'getting:', key
    return
pinata = Pinata()

class WaitForKey:
  def main(self):
    # Return a single character from stdin.

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

class IsLetter:
  def main(self, ch):
    return ch.isalpha()

class FindAllFiles:
  def __init__(self, kw):
    self.path_to_text = {}

    for path in glob.glob(os.path.join(kw['dir_path'], '*')):
      with open(path) as f:
        text = f.read()
      self.path_to_text[path] = text.lower()

  def main(self, dir_path, query_string):
    matches = []
    query_lower = query_string.lower()

    for path in glob.glob(os.path.join(dir_path, '*')):
      if query_lower in path:
        matches.append(path)

      if query_string in self.path_to_text:
        matches.append(path)
    return matches

if __name__ == '__main__':
  init(dir_path='.')
