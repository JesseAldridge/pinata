import os

from pinata import pinata

def main():
  query_string = ''
  dir_path = os.path.expanduser('~/Dropbox/tbrush_notes')
  Pinata.init_find_all_files(dir_path)

  while True:
    print 'query_string: [{}]'.format(query_string)
    ch = Pinata.wait_for_key()
    if Pinata.is_letter(ch):
      query_string += ch
    print Pinata.find_all_files(query_string)

if __name__ == '__main__':
  main()
