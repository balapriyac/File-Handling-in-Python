with open('lib.txt','r') as f:
  line = f.readline()
  print(line)
  f.seek(0)
  line = f.readline()
  print(line)
