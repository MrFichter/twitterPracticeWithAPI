##@Fictitious suggested that the code below would be a good
##starting point.
###Next step: comb through it, see what each line does, and
###document it. (Start with main.py, though.)


##I would use this line if I were running the program in Linux: #!/usr/bin/env python

import os
import marshal

BACKUP = os.path.join(os.path.dirname(__file__), 'backup.mrsh') ###Would I need to replace "dirname" and "file" with an actual directory name and file?

def save(d):
  backup = open(BACKUP, 'w')
  marshal.dump(d, backup)
  backup.close()

def load():
  return marshal.load(open(BACKUP))

def main():
  d = {'a' :
        {1 : 'x',
         2 : 'y'},
       'b' :
        {1 : 'z'}}
  print(d)
  save(d)
  d = load()
  print(d)
  d['c'] = {3 : 'w'}
  save(d)
  d = load()
  print(d)

if __name__ == '__main__':
  main()
