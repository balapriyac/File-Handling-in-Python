chunk_size = 50
with open('lib.txt','r') as f:
  chunk = f.read(chunk_size)
  print(chunk,end='')

  while(len(chunk)>0):
    chunk = f.read(chunk_size)
    print(chunk,end='')
