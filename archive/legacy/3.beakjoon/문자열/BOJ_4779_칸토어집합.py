def list_split(arr ,n):
   return [arr[i : i+n] for i in range(0, len(arr), n)]

def Cantor(line):
   if len(line) == 1:
      print(line,end='')
      return 
   else:
      split_line = list_split(line,len(line)//3)
      for i in range(len(split_line)):
        if i == 1: 
            split_line[i] = split_line[i].replace("-"," ")
        Cantor(split_line[i])
      

while True:
    try:
        n = int(input())
        init_line = "-" * (3**(n))
        Cantor(init_line)
        print()

    except EOFError:
        break
