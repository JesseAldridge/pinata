class ReadFile:
  def main(self):
    def read_file(path):
      with open(path) as f:
        return f.read()
    return [read_file]

  def description(self):
    return 'Read the contents of a file on the filesystem'
