import shutil, os

from pinata2 import pinata

assert pinata.is_letter('a') == True
assert pinata.is_letter('1') == False
assert pinata.is_letter('#') == False

simulate_keystroke('a')
assert pinata.wait_for_key() == 'a'

if not os.path.exists('test_dir'):
  os.mkdir('test_dir')
try:
  with open('test_dir/1.txt', 'w') as f:
    f.write('some text')
  with open('test_dir/2.txt', 'w') as f:
    f.write('other text')
  pinata.init_find_all_files('test_dir')
  assert pinata.find_all_files('some') == ['test_dir/1.txt']
  assert pinata.find_all_files('other') == ['test_dir/2.txt']
  assert pinata.find_all_files('nothing') == []
finally:
  shutil.rmtree('test_dir')
