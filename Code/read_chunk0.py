chunk_size = 50
with open('lib.txt','r') as f:
  chunk = f.read(chunk_size)
  print(chunk)
  current = f.tell()
  print(f"Current position of file pointer: {current}")
