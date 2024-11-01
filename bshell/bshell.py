import os

# This is BShell

inp_val = ''
try:
  inp_val = input("SDir(Session-Directory)# ")
  os.chdir(inp_val)
except:
  inp_val = ''
  print('Avoided Errors.\n')
while True:
  try:
    inp = input(inp_val + '# ')
    if inp == 'exit':
      break
    elif inp.startswith('echo ') == True:
      print(inp.removeprefix('echo '))
    elif inp.startswith('csd ') == True:
      try:
        os.chdir(os.getcwd()+'\\'+inp.removeprefix('csd '))
        inp_val = os.getcwd()
      except:
        pass
    elif inp.startswith('cd ') == True:
      os.chdir(inp.removeprefix('cd '))
      inp_val = os.getcwd()
    elif inp.startswith('mkdir ') == True:
      os.mkdir(inp.removeprefix('mkdir '))
    elif inp.startswith('rmdir ') == True:
      os.rmdir(inp.removeprefix('rmdir '))
    elif inp.startswith('tch ') == True:
      f = open(inp.removeprefix('tch '), 'w')
      f.close()
    elif inp == 'cwd':
      print(os.getcwd())
    elif inp.startswith('rd ') == True:
      f = open(inp.removeprefix('rd '), 'r')
      print(f.read())
      f.close()
    elif inp == 'map':
      for root, directories, files in os.walk(os.getcwd()):
        print(f"Directory: {root}")
        for file in files:
            print(f"--> File: {file}")
    else:
      print("Error: Invalid Command.\n")
  except OSError as err:
    print(err)
    print('Avoided Errors.\n')
