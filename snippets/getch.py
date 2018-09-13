import sys, termios, tty

class Getch:
  def main(self):
    def getch():
      # Return a single character from stdin.

      fd = sys.stdin.fileno()
      old_settings = termios.tcgetattr(fd)
      try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
      finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
      return ch

    return getch

  def description(self):
    return 'wait for the user to type a key'
